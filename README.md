# CodeQL + Checkov Security Scanning Proof of Concept

⚠️ **Important**

All vulnerabilities in this repository are **intentionally introduced for demonstration purposes only**.  
The code and infrastructure examples are **not intended to be executed in production environments**.

---

## Overview

This repository demonstrates how modern DevSecOps security scanning tools can identify vulnerabilities and misconfigurations across the **entire software delivery lifecycle**.

The examples intentionally include insecure application code, CI/CD configurations, and infrastructure definitions so security scanners can detect realistic security issues.

**All findings are visible in:**  
`Security → Code scanning`

---

## DevSecOps Security Coverage

This repository illustrates how automated security scanning can identify risks throughout the development pipeline:

```
Application Code
      ↓
Cryptographic Implementation
      ↓
File System Access
      ↓
Command Execution
      ↓
CI/CD Pipeline Configuration
      ↓
Infrastructure as Code
      ↓
Cloud Security Configuration
      ↓
Identity and Access Control
      ↓
Logging and Monitoring Controls
```

The alerts generated from this repository demonstrate how automated security tooling can detect vulnerabilities **before they reach production environments**.

---

## Tools Demonstrated

| Tool | Purpose |
|-----|--------|
| **CodeQL** | Static analysis for application code and CI/CD workflow security |
| **Checkov** | Infrastructure‑as‑Code security scanning for Terraform and cloud resources |

---

## Security Coverage

### Application Security (CodeQL)

| Vulnerability Class | Example |
|---------------------|--------|
| SQL Injection | SQL query built from user‑controlled input |
| Command Injection | Uncontrolled command line execution |
| Path Traversal | Uncontrolled data used in path expression |
| Weak Cryptography | Use of broken or weak hashing algorithm |

---

### CI/CD Pipeline Security (CodeQL)

| Risk | Example |
|-----|--------|
| Missing workflow permissions | GitHub workflow without explicit permission block |
| Supply chain integrity | Unpinned GitHub Action version |

---

### Infrastructure as Code (Checkov)

| Cloud Security Risk | Example |
|--------------------|--------|
| Network exposure | Open security group |
| Storage exposure | Public S3 bucket |
| Encryption failure | Unencrypted EBS volume |
| Identity privilege escalation | Overly permissive IAM policy |
| Logging / monitoring gaps | CloudTrail logging disabled |

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

This repository is intended for:

- **DevSecOps demonstrations**
- **Security tooling evaluations**
- **Security awareness and training**
- **Example vulnerability detection workflows**

All vulnerabilities are **deliberately included** so that automated scanners generate alerts that can be reviewed in the GitHub Security dashboard.
