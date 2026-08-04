# pip-audit Dependency Scan Report

## Report Information

| Field | Value |
|---|---|
| Project | DevSecOps Engineering |
| Week | Week 4 |
| Application | Python Flask Web Application |
| Scanner | pip-audit |
| Initial manifest | src/week-4/requirements-vulnerable.txt |
| Final manifest | src/week-4/requirements.txt |
| Initial text report | report/week4-vulnerable-scan.txt |
| Initial JSON report | report/week4-vulnerable-scan.json |
| Final text report | report/week4-clean-scan.txt |
| Final JSON report | report/week4-clean-scan.json |

## Scan Scope

The scan covered the Python packages listed in the Week 4 dependency
manifests.

The initial scan used a deliberately outdated dependency version to
demonstrate vulnerability detection.

The final scan used the remediated and fully pinned application dependencies.

## Tool Verification

The installed scanner version was checked using:

```powershell
& .\.security-tools\Scripts\python.exe -m pip_audit --version
```

Tool version:

```text
[REPLACE WITH THE CONTENT OF report/week4-tool-version.txt]
```

## Initial Vulnerable Dependency

The controlled demonstration used:

```text
Flask==0.5
```

This outdated package was used only for scanning and was not installed or
deployed as part of the final application.

## Initial Scan Command

```powershell
& .\.security-tools\Scripts\python.exe -m pip_audit `
    -r .\src\week-4\requirements-vulnerable.txt `
    --no-deps `
    --aliases on `
    --desc on
```

## Initial Scan Result

```text
[PASTE THE EXACT CONTENT OF report/week4-vulnerable-scan.txt]
```

## Vulnerability Findings

Complete this table using the actual output from the initial scan.

| Package | Vulnerable Version | Vulnerability ID | Alias or CVE | Fix Version | Status |
|---|---:|---|---|---:|---|
| [ACTUAL PACKAGE] | [VERSION] | [ADVISORY ID] | [CVE IF DISPLAYED] | [FIX VERSION] | Remediated |
| [ADD MORE ROWS WHEN REQUIRED] | | | | | |

## Finding Analysis

The initial scan confirmed that outdated third-party packages may contain
publicly known vulnerabilities.

The scanner provided the installed package version, vulnerability identifier,
available aliases, description, and fixed version information.

## Risk Level

Using vulnerable dependencies can expose the application to:

- Unauthorized access
- Information disclosure
- Integrity compromise
- Application instability
- Denial-of-service conditions
- Software supply-chain attacks

The exact risk depends on the affected package, vulnerability type, severity,
and how the application uses the component.

## Remediation Actions

The following remediation actions were completed:

1. The outdated dependency was used only in a controlled scan.
2. The vulnerability findings were saved as text and JSON.
3. A clean Python virtual environment was created.
4. A current compatible Flask release was installed.
5. Transitive dependencies were resolved.
6. All final dependencies were pinned.
7. The final dependency set was rescanned.
8. The temporary vulnerable manifest was removed.

## Final Scan Command

```powershell
& .\.security-tools\Scripts\python.exe -m pip_audit `
    -r .\src\week-4\requirements.txt `
    --no-deps `
    --aliases on `
    --desc on
```

## Final Scan Result

```text
[PASTE THE EXACT CONTENT OF report/week4-clean-scan.txt]
```

## Comparison

| Area | Initial Scan | Final Scan |
|---|---|---|
| Manifest | Temporary vulnerable manifest | Final pinned manifest |
| Dependency state | Outdated dependency | Current compatible dependencies |
| Vulnerabilities | Known findings detected | [ACTUAL FINAL RESULT] |
| Deployment status | Not deployed | Application dependency set |
| Report format | Text and JSON | Text and JSON |

## Evidence

### Initial vulnerable scan

![Initial scan](../../evidence/week-4/05-pip-audit-vulnerable-scan.png)

### JSON report

![JSON report](../../evidence/week-4/06-vulnerability-report-generated.png)

### Final scan

![Final scan](../../evidence/week-4/10-clean-dependency-scan.png)

## Conclusion

`pip-audit` successfully detected known vulnerabilities in the controlled
outdated dependency. The vulnerable component was replaced with current
compatible dependencies, and the final dependency set was scanned again to
verify remediation.