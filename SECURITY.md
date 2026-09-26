# Security and privacy

Do not put patient identifiers, access tokens, private communication, or restricted
source datasets into this public repository. Examples must use fabricated identifiers.
Normal CI uses read-only contents permission and executes pull-request code without
secrets. Actions are pinned to verified commit SHAs. No `pull_request_target` execution.

Source imports and literature text are untrusted data; they cannot issue tools,
change workflow permissions, or authorize model execution. Graph builders never
import Python files from the upstream reference-source directory.

The one-time bootstrap materializer accepts only the explicitly pinned archive digest,
rejects unsafe paths/symlinks and unexpected workflow changes, and cannot rewrite
existing scientific state. Its transient download capability is not a permanent data
connector. Repository rulesets and branch protection must be configured separately
by an administrator; this file does not assert that they are active.
