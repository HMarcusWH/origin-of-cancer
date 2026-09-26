# Contributing

## Scientific changes

Use a branch and pull request. Identify affected stable IDs, source locators, scope,
assumptions, nulls, evidence class, data uses, claim ceilings, and negative-result
consequences. Preserve original source snapshots. A paper summary does not directly
promote a claim; add a reviewed EvidenceAssessment and scoped Verdict.

## Engineering checks

```bash
python -m pip install -r requirements.txt
python tools/build.py --check
python tools/validate.py
python -m unittest discover -s tests -v
```

For an intentional authored change, regenerate with `python tools/build.py --write`,
then rerun checks. Never hand-edit generated current-state or coverage files. Runtime
build/validation are offline and never execute upstream reference code.

## Review

The author of a new scientific claim should not be counted as independent validation.
A contributor must distinguish theory inheritance from evidence, an engineering
regression from an experiment, and a scoped model result from biology. Report defects
with a minimal reproducible fixture. Do not upload patient-level information or secrets.

Do not close an RG item merely because its document exists. Scientific OPEN is allowed;
malformed records, stale output, missing provenance and unsupported promotion are not.
