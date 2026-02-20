from pydantic import BaseModel
from typing import List
from datetime import datetime

class ChangeRequest(BaseModel):
    change_id: str
    service: str
    env: str
    window_start: datetime
    window_end: datetime
    pii: bool = False
    internet_exposed: bool = False
    db_migration: bool = False
    schema_change: bool = False
    uses_feature_flag: bool = True
    has_rollback: bool = True
    has_runbook: bool = True
    blast_radius: str = "medium"
    changes: List[str] = []

class GuardrailResponse(BaseModel):
    change_id: str
    risk_score: int
    risk_band: str
    risk_factors: List[str]
    risk_contributions: List[dict]
    top_contributors: List[dict]
    required_approvals: List[str]
    approval_reasons: List[dict]
    release_plan: dict