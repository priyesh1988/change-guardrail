from fastapi import FastAPI
from .models import ChangeRequest, GuardrailResponse
from .risk import compute_risk, risk_band, build_release_plan
from .policy import load_policy, eval_condition

app = FastAPI(title="Change Risk Guardrail")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/guardrail", response_model=GuardrailResponse)
def guardrail(cr: ChangeRequest):
    score, factors, contribs = compute_risk(cr)
    band = risk_band(score)

    ctx = {
        "env": cr.env,
        "pii": cr.pii,
        "internet_exposed": cr.internet_exposed,
        "db_migration": cr.db_migration,
        "schema_change": cr.schema_change,
        "risk_score": score,
    }

    pol = load_policy()
    approvals = set()
    approval_reasons = []

    for rule in pol["approval_rules"]:
        if eval_condition(rule["if"], ctx):
            for a in rule["require"]:
                approvals.add(a)
                approval_reasons.append({"approval": a, "because": rule["if"]})

    top = sorted(contribs, key=lambda x: x["delta"], reverse=True)[:3]

    return GuardrailResponse(
        change_id=cr.change_id,
        risk_score=score,
        risk_band=band,
        risk_factors=factors,
        risk_contributions=contribs,
        top_contributors=top,
        required_approvals=sorted(list(approvals)),
        approval_reasons=approval_reasons,
        release_plan=build_release_plan(),
    )