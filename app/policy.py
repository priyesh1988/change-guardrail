import yaml
from pathlib import Path

POLICY_PATH = Path("policies/rules.yaml")

def load_policy():
    with open(POLICY_PATH, "r") as f:
        return yaml.safe_load(f)

def eval_condition(expr, ctx):
    allowed = {"True": True, "False": False}
    allowed.update(ctx)
    return bool(eval(expr, {"__builtins__": {}}, allowed))