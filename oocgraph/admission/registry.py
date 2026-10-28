"""Fail-closed admission sink inventory: new schema-positive paths need policy owners."""
import json
from pathlib import Path

# A new positive enum value matching these names cannot silently bypass review.
POSITIVE_KEYS = {
    ('Verdict','decision'): {'SUPPORTED_SCOPED','MATHEMATICALLY_VERIFIED_SCOPED'},
    ('Transition','status'): {'SUPPORTED_SCOPED'},
    ('Route','status'): {'CLOSED'},
    ('ModelInstance','status'): {'ADMITTED'},
    ('DataUse','status'): {'ADMITTED'},
    ('Requirement','status'): {'SATISFIED','BOUNDED'},
    ('ResearchGap','status'): {'RESOLVED','BOUNDED'},
    ('AuthorizationEvent','action'): {'ADMIT_MODEL','FREEZE_KERNEL'},
    ('SourceVerification','status'): {'VERIFIED'},
    ('LiteratureSource','bibliographic_verification'): {'VERIFIED'},
    ('LiteratureSource','extraction_status'): {'EXTRACTED'},
    ('Claim','empirical_admission'): {'RECORDED_IN_VERDICTS'},
    ('Theory','status'): {'CARD_COMPLETE'},
    ('Adapter','status'): {'DOSSIER_COMPLETE'},
    ('Result','status'): {'VALIDATED'},
    ('Relation','kind'): {'SUPPORTS'},
}

# Any newly added status containing one of these strings in an audited field
# is treated as a promotion candidate pending policy review.
SUSPECT = ('SUPPORT','ADMIT','VERIFY','VERIFIED','CLOSED','SATISF','RESOLV','BOUNDED',
           'FREEZE','EXTRACTED','COMPLETE','VALIDATED')


def enumerate_sinks(schema):
    entries=[]
    audited_fields={"status","decision","action","bibliographic_verification",
                    "empirical_admission","extraction_status","kind"}
    for typ,definition in schema.get('$defs',{}).items():
        for field,shape in definition.get('properties',{}).items():
            if field not in audited_fields or field == 'kind' and typ != 'Relation':
                continue
            required = POSITIVE_KEYS.get((typ,field),set())
            for value in shape.get('enum',[]):
                if value in required or (isinstance(value,str) and any(
                        word in value for word in SUSPECT)):
                    entries.append(f'{typ}.{field}:{value}')
    entries.append('Programme.kernel_frozen:true')
    return tuple(sorted(set(entries)))

def registry_errors(root):
    root=Path(root)
    if not (root/'config/promotion_path_registry.json').is_file():
        return ['MISSING_PROMOTION_PATH_REGISTRY']
    schema=json.loads((root/'schema/graph-record.schema.json').read_text())
    cfg=json.loads((root/'config/promotion_path_registry.json').read_text())
    registered={item.get('id') for item in cfg.get('sinks',[])}
    actual=set(enumerate_sinks(schema))
    errors=[f'UNREGISTERED_SCIENTIFIC_PROMOTION:{x}' for x in sorted(actual-registered)]
    errors.extend(f'ORPHANED_PROMOTION_POLICY:{x}' for x in sorted(registered-actual))
    from .. import core
    for item in cfg.get('sinks',[]):
        if not item.get('policy_id') or not item.get('mode') or not item.get('owner'):
            errors.append('INCOMPLETE_PROMOTION_POLICY:'+str(item.get('id')))
        if item.get('mode') not in {'AUTHORITATIVE','NON_AUTHORITATIVE_METADATA','HISTORICAL_ONLY'}:
            errors.append('UNDEFINED_PROMOTION_MODE:'+str(item.get('id')))
        expected = 'NON_AUTHORITATIVE_ONLY' if item.get('mode') != 'AUTHORITATIVE' else None
        evaluator = item.get('evaluator')
        if expected and evaluator != expected:
            errors.append('METADATA_CONFUSED_WITH_SCIENTIFIC_ADMISSION:'+str(item.get('id')))
        if not expected and (not isinstance(evaluator,str)
                             or not evaluator.startswith(('effective_','_historical_','resolve'))
                             or not callable(getattr(core,evaluator,None))):
            errors.append('UNOWNED_SCIENTIFIC_ADMISSION_EVALUATOR:'+str(item.get('id')))
    return errors
