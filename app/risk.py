from .policy import load_policy

def risk_band(score):
    if score < 30: return "LOW"
    if score < 60: return "MEDIUM"
    if score < 80: return "HIGH"
    return "CRITICAL"

def compute_risk(cr):
    pol = load_policy()
    w = pol["risk_weights"]
    score = 0
    factors = []
    contribs = []

    def add(label, delta):
        nonlocal score
        score += delta
        factors.append(label)
        contribs.append({"label": label, "delta": delta})

    if cr.env == "prod": add("Production change", w["prod"])
    if cr.pii: add("Handles PII", w["pii"])
    if cr.internet_exposed: add("Internet exposed", w["internet_exposed"])
    if cr.db_migration: add("DB migration", w["db_migration"])
    if cr.schema_change: add("Schema change", w["schema_change"])
    if cr.uses_feature_flag: add("Feature flag mitigation", w["uses_feature_flag"])
    if cr.has_rollback: add("Rollback defined", w["has_rollback"])
    if cr.has_runbook: add("Runbook available", w["has_runbook"])
    if cr.blast_radius == "high": add("High blast radius", w["high_blast_radius"])

    score = max(0, min(100, score))
    return score, factors, contribs

def build_release_plan():
    return load_policy()["release_plan_templates"]["default"]