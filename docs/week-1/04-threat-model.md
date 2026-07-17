# Week 1 Threat Model

## 1. Scope

This threat model covers the Git and GitHub workflow used for the DevSecOps
Engineering project.

## 2. System Workflow

```mermaid
flowchart LR
    A[Developer] --> B[Local Workstation]
    B --> C[Local Git Repository]
    C --> D[Feature Branch]
    D --> E[GitHub Repository]
    E --> F[Pull Request]
    F --> G[Review]
    G --> H[Main Branch]