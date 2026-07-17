# Secure SDLC Security Gates

## 1. Purpose

Security gates are conditions that must be completed before work proceeds to
the next development stage.

## 2. Requirements Gate

Required activities:

- Security requirements documented
- Assets identified
- Initial risks recorded
- Security responsibilities identified

Pass criteria:

- Required documentation exists.
- Requirements have unique identifiers.
- Important risks are recorded.

Week 1 status: Completed

## 3. Design Gate

Required activities:

- System workflow documented
- Threat model created
- Trust boundaries identified
- Important security controls selected

Pass criteria:

- Threat model exists.
- STRIDE threats are documented.
- Recommended controls are identified.

Week 1 status: Completed

## 4. Development Gate

Required activities:

- Git repository initialized
- `.gitignore` configured
- No secrets added
- Meaningful commit messages used
- Separate branch used

Pass criteria:

- Git status is reviewed.
- Sensitive files are excluded.
- Changes are committed with meaningful messages.

Week 1 status: In Progress

## 5. Pull-Request Gate

Required activities:

- Changes reviewed
- Files Changed tab checked
- Security checklist completed
- No sensitive information included

Pass criteria:

- Pull request is reviewed.
- Required documentation is complete.
- No secrets are visible.

Week 1 status: In Progress

## 6. Security-Testing Gate

Planned future activities:

- Static application security testing
- Dependency scanning
- Secret scanning
- Dynamic security testing

Status: Planned for future weeks

## 7. Release Gate

Required activities:

- Critical findings resolved
- Documentation completed
- Required evidence collected
- Release approved

Status: Planned for future weeks

## 8. Pull-Request Security Checklist

- [ ] No passwords, tokens, or private keys were added.
- [ ] `.gitignore` is correctly configured.
- [ ] Changes were reviewed using `git diff`.
- [ ] Commit messages are meaningful.
- [ ] Documentation was updated.
- [ ] Evidence does not contain sensitive information.
- [ ] Only required files were changed.

## 9. Conclusion

Security gates help prevent incomplete or insecure work from progressing
through the development lifecycle.