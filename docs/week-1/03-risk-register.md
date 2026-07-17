# Initial Cybersecurity Risk Register

## 1. Purpose

This risk register records initial cybersecurity risks associated with the
DevSecOps Engineering project.

## 2. Risk-Scoring Method

Risk Score = Likelihood × Impact

Likelihood and impact are rated from 1 to 5.

| Score | Risk Level |
|---:|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–15 | High |
| 16–25 | Critical |

## 3. Initial Risk Register

| ID | Risk | Likelihood | Impact | Score | Level | Control | Status |
|---|---|---:|---:|---:|---|---|---|
| R-01 | Secret committed to GitHub | 4 | 5 | 20 | Critical | `.gitignore`, policy, review | Open |
| R-02 | Unauthorized GitHub account access | 3 | 5 | 15 | High | Strong password and 2FA | Open |
| R-03 | Direct unreviewed change to main | 3 | 5 | 15 | High | Branch and pull-request workflow | Open |
| R-04 | Accidental deletion of project files | 2 | 3 | 6 | Medium | Git history and GitHub remote | Open |
| R-05 | Sensitive screenshot uploaded | 3 | 4 | 12 | High | Screenshot review | Open |
| R-06 | Incomplete documentation | 3 | 3 | 9 | Medium | Completion checklist | Open |
| R-07 | Incorrect repository permissions | 3 | 5 | 15 | High | Access-control review | Open |
| R-08 | Unclear commit history | 3 | 2 | 6 | Medium | Meaningful commit messages | Open |
| R-09 | Malicious or incorrect pull request | 2 | 5 | 10 | High | Pull-request review | Open |
| R-10 | Vulnerable dependency | 4 | 4 | 16 | Critical | Dependency scanning in a future week | Planned |
| R-11 | Insecure CI/CD configuration | 3 | 5 | 15 | High | CI/CD security review in a future week | Planned |
| R-12 | Local workstation compromise | 3 | 5 | 15 | High | Updates, authentication, and antivirus | Open |

## 4. Risk-Treatment Options

- **Avoid:** Stop the risky activity.
- **Mitigate:** Apply controls to reduce likelihood or impact.
- **Transfer:** Transfer part of the risk to another party or service.
- **Accept:** Formally accept the remaining risk.

## 5. Week 1 Risk Treatment

The main Week 1 risk-treatment actions are:

- Use `.gitignore`.
- Avoid committing secrets.
- Use meaningful commits.
- Use Git history.
- Create separate branches.
- Review changes before merging.
- Keep evidence free from sensitive information.

## 6. Conclusion

The risk register helps prioritize security work. Security controls reduce risk,
but they do not guarantee that risk is completely eliminated.