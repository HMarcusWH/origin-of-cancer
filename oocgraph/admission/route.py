"""Independent witness reachability primitive, with explicit admissible alternatives."""

def has_ancestry_path(segment_keys, ancestry_keys, *, allowed_labels=None, successors=None):
    """Find a path through all segments, returning one certificate path or None.

    Empty/unproven paths never qualify.  A valid optional witness does not
    invalidate another continuous ancestry-supported path.
    """
    if not segment_keys or not ancestry_keys:
        return None
    frontier = {key: (key,) for key in segment_keys[0] & set(ancestry_keys)}
    if allowed_labels is not None:
        frontier = {k:p for k,p in frontier.items() if k[2] in allowed_labels}
    if not frontier:
        return None
    for i in range(len(segment_keys)-1):
        nxt = segment_keys[i+1]
        advanced = {}
        for key,path in sorted(frontier.items()):
            if key in nxt:
                advanced[key] = path + (key,)
            if successors is not None:
                for successor in successors(i, {key}, nxt):
                    if successor in nxt:
                        advanced[successor] = path + (successor,)
        frontier = advanced
        if not frontier:
            return None
    if allowed_labels is not None:
        frontier = {k:p for k,p in frontier.items() if k[2] in allowed_labels}
    return min(frontier.values()) if frontier else None
