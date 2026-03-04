# CodeQL + Checkov Security Scanning PoC

## Overview
This repository demonstrates how security scanning tools can identify vulnerabilities across different parts of a modern software delivery pipeline.

The examples intentionally include insecure code and infrastructure configurations so scanners can detect realistic security issues.

**All findings are visible in:**  
Security → Code scanning

---

## Tools Demonstrated

| Tool | Purpose |
|---|---|
| CodeQL | Static application and CI/CD security scanning |
| Checkov | Infrastructure-as-Code security scanning |

---

## Security Areas Covered

| Security Area | Example |
|---|---|
| Application security | SQL injection in a Python Flask example |
| CI/CD pipeline security | GitHub Actions workflow misconfigurations |
| Supply chain security | Unpinned GitHub Action |
| Infrastructure security | Terraform cloud misconfigurations (network, storage, encryption, IAM) |

---

## Repository Structure

```
.github/workflows/
csharp_examples/
python_examples/
iac_examples/terraform/
README.md
LICENSE
```

---

## Purpose
This repository is intended for DevSecOps demonstrations, security tool evaluation, and training/education.  
All vulnerabilities are intentionally included.
