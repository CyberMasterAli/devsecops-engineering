# CI/CD Security Proof of Concept

## Objective

The objective was to demonstrate that the CI/CD pipeline
automatically blocks an insecure change.

## Test

A demonstration .env file containing a fake value was
intentionally added to Git.

## Detection

The CI-CD Policy Check detected that an .env file was
being tracked.

## Result

The GitHub Actions workflow failed and the pull request
did not satisfy the required security checks.

## Remediation

The tracked .env file was removed.

## Verification

The updated code was pushed again and all required
CI/CD security checks passed.

## Conclusion

The experiment demonstrated that security controls are
automatically enforced before code is allowed to progress
through the delivery pipeline.