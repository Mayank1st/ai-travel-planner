# To skip from hardcoded if-else statement, in case of multiple workflows
from app.workflows.travel_workflow import run_travel_workflow

WORKFLOW_REGISTRY = {"travel": run_travel_workflow}
