# Change Risk Guardrail
## Production Change Risk Intelligence Platform

A policy-driven, auditable, and deterministic change risk evaluation service designed for enterprise engineering organizations.

This platform evaluates production change requests and produces:

- Risk score (0–100)
- Risk band (LOW / MEDIUM / HIGH / CRITICAL)
- Required approvals (CAB, SRE, Security, DBA, VP)
- Structured release plan (prechecks, rollout, rollback)
- Explainable risk contributions
- Approval reasoning
- Audit log trail

---

## Summary

Modern engineering organizations move fast — but unmanaged change risk leads to:

- Production incidents  
- Compliance violations  
- Escalations to senior leadership  
- Audit findings  

This service standardizes change governance using **policy-as-code** and deterministic risk modeling.

Instead of subjective review meetings, this system produces consistent, explainable, and auditable decisions.

---

## Key Capabilities

### Deterministic Risk Scoring
Risk is computed from structured inputs:

- Production vs non-production
- PII exposure
- Internet exposure
- Database migrations
- Schema changes
- Blast radius
- Change window timing
- Mitigation controls (feature flags, rollback, runbooks)

Every score is explainable and reproducible.

---

### Policy-as-Code Approval Engine
Approval requirements are driven by YAML policies:

- CAB for high-risk production changes  
- Security for PII or internet exposure  
- DBA for schema or database changes  
- Executive escalation for critical risk  

No hardcoded logic. Fully configurable.

---

### Explainability Layer

Each response includes:

- Individual risk contributions (delta values)
- Top contributors
- Approval reasons mapped to rule expressions

Example:

```json
{
  "risk_score": 78,
  "risk_band": "HIGH",
  "top_contributors": [
    {"label": "DB migration", "delta": 20},
    {"label": "Production change", "delta": 20},
    {"label": "High blast radius", "delta": 20}
  ],
  "approval_reasons": [
    {"approval": "CAB", "because": "env == 'prod' and risk_score >= 60"},
    {"approval": "SECURITY", "because": "pii == True or internet_exposed == True"}
  ]
}
```

---

## Architecture Overview

| Layer | Technology |
|-------|------------|
| API Layer | FastAPI |
| Risk Engine | Deterministic scoring module |
| Policy Engine | YAML policy rules |
| Governance | Rule-based approval evaluator |
| Audit | Structured JSON logs |
| CI | GitHub Actions (ruff + pytest) |

This service is intentionally lightweight and stateless, making it easy to:

- Integrate into CI/CD pipelines  
- Trigger from change management systems  
- Embed into internal portals  
- Extend with RBAC or persistence  

---

## API Endpoints

### Health Check
```
GET /health
```

### Evaluate Guardrail
```
POST /guardrail
```

Example request body:

```json
{
  "change_id": "CHG-123456",
  "service": "payments-ledger-api",
  "env": "prod",
  "window_start": "2026-02-19T10:00:00Z",
  "window_end": "2026-02-19T11:00:00Z",
  "pii": true,
  "internet_exposed": true,
  "db_migration": true,
  "schema_change": false,
  "uses_feature_flag": true,
  "has_rollback": true,
  "has_runbook": true,
  "blast_radius": "high",
  "changes": ["new endpoint", "db index change"]
}
```

---

## Quick Start

Install dependencies:

```
pip install -r requirements.txt
```

Run service:

```
uvicorn app.main:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Continuous Integration

CI pipeline includes:

- Ruff linting
- Pytest unit tests
- Python 3.12 validation

Configured in:

```
.github/workflows/ci.yml
```

---

## Design Principles

Deterministic over probabilistic  
Policy-driven over manual review  
Explainable over opaque  
Auditable over tribal knowledge  

---

## Strategic Impact

This platform shifts change management from reactive review to proactive risk intelligence.

It enables:

- Faster safe releases  
- Reduced incident frequency  
- Standardized governance  
- Leadership visibility  
- Audit readiness  

---

## Future Enhancements

- OPA integration (replace YAML evaluator)
- Persistent audit storage (Postgres / SIEM)
- RBAC integration
- Service dependency graph risk modeling
- Historical risk trend analytics
- Executive dashboard view
- ChatOps integration (Slack / Teams)

---

Built for enterprise-scale engineering governance.
