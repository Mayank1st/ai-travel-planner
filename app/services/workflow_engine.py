from app.registry.workflow_registry import WORKFLOW_REGISTRY


# Workflow Engine
async def execute_workflow(workflow_name: str, payload: dict):
    workflow = WORKFLOW_REGISTRY[workflow_name]
    return await workflow(**payload)
