
# Secure Software Development Life Cycle

## 1. Introduction

The Software Development Life Cycle is a structured process used to plan,
design, develop, test, deploy, maintain, and retire software systems.

A Secure Software Development Life Cycle integrates security into every phase
of development. Security is not treated only as a final testing activity.
Security requirements, risks, reviews, and controls are considered from the
beginning of the project.

## 2. Traditional SDLC and Secure SDLC

| Traditional SDLC | Secure SDLC |
|---|---|
| Focuses mainly on functionality | Includes functionality and security |
| Security may be reviewed near release | Security begins during planning |
| Risks may be identified late | Risks are identified early |
| Security is treated separately | Security is integrated into every phase |
| Limited security documentation | Requirements, risks, and controls are documented |
| Vulnerabilities may be expensive to fix | Earlier detection reduces remediation effort |

## 3. Shift-Left Security

Shift-left security means performing security activities earlier in the
development lifecycle. Examples include defining security requirements during
planning, performing threat modelling during design, and reviewing code during
development.

Early security activities reduce the likelihood that serious vulnerabilities
will remain undetected until deployment.

## 4. Secure SDLC Phases

### 4.1 Planning and Requirements

Development activities:

- Define business objectives.
- Define users and project scope.
- Identify required features.

Security activities:

- Identify sensitive assets.
- Define security requirements.
- Identify legal or privacy obligations.
- Record initial security risks.
- Assign security responsibilities.

### 4.2 Secure Design

Development activities:

- Design the system architecture.
- Select technologies.
- Design APIs and databases.

Security activities:

- Perform threat modelling.
- Identify trust boundaries.
- Plan authentication and authorization.
- Apply least privilege.
- Reduce unnecessary attack surfaces.

### 4.3 Secure Development

Development activities:

- Write and review application code.
- Create project files and configurations.

Security activities:

- Follow secure coding practices.
- Validate untrusted input.
- Avoid hard-coded credentials.
- Use version control.
- Review code changes.
- Use meaningful commits.

### 4.4 Security Verification

Development activities:

- Confirm that features work correctly.

Security activities:

- Review security requirements.
- Perform security testing.
- Review dependencies.
- Check for exposed secrets.
- Record and remediate findings.

Static testing and dependency scanning are planned for later internship weeks.

### 4.5 Secure Deployment

Security activities:

- Protect deployment credentials.
- Disable unnecessary services.
- Use secure configurations.
- Restrict permissions.
- Prepare rollback procedures.
- Avoid exposing debugging information.

### 4.6 Operations and Maintenance

Security activities:

- Monitor application logs.
- Review security alerts.
- Patch vulnerabilities.
- Update dependencies.
- Respond to incidents.
- Rotate exposed credentials.

### 4.7 Retirement

Security activities:

- Revoke credentials.
- Remove unused services.
- Archive required records.
- Securely delete sensitive information.
- Remove unnecessary access.

## 5. Security Principles

### Least Privilege

Users and systems should only receive the permissions required to perform their
assigned responsibilities.

### Defence in Depth

Multiple security controls should protect important assets. A single security
control should not be considered sufficient.

### Secure by Default

Default configurations should provide safe and restricted behavior.

### Separation of Duties

Sensitive changes should be reviewed or approved by another authorized person
where possible.

### Continuous Improvement

Security risks, controls, and processes should be reviewed throughout the
software lifecycle.

## 6. Week 1 Implementation

During Week 1, the following Secure SDLC foundation was established:

- Initial security requirements were documented.
- An initial risk register was created.
- A basic threat model was prepared.
- Security gates were defined.
- Git was selected for traceable change management.
- GitHub was selected for remote repository management.
- Sensitive files were excluded using `.gitignore`.

## 7. Secure SDLC Diagram

```mermaid
flowchart LR
    A[Planning and Requirements] --> B[Secure Design]
    B --> C[Secure Development]
    C --> D[Security Verification]
    D --> E[Secure Deployment]
    E --> F[Operations and Maintenance]
    F --> G[Retirement]
    F --> A