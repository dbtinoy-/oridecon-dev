---
title: oridecon-workflow How-Tos
description: Task-oriented recipes for pipelines, graphs, sagas, and bulk operations
---

## How to create a multi-step pipeline

```python
from oridecon.workflow import Pipeline, step

pipeline = Pipeline()

@step(name="fetch")
async def fetch(ctx: dict) -> dict:
    return {"data": {"user": "alice", "score": 95}}

@step(name="enrich")
async def enrich(ctx: dict) -> str:
    user = ctx["fetch"]["data"]["user"]
    score = ctx["fetch"]["data"]["score"]
    return f"{user}: {score}/100"

pipeline.add_step(fetch)
pipeline.add_step(enrich)

result = await pipeline.execute()
print(result)  # "alice: 95/100"
```

## How to add conditional branching in a pipeline

```python
from oridecon.workflow import conditional

@conditional(
    name="route",
    condition=lambda ctx: ctx.get("is_premium", False),
)
async def premium_path(ctx: dict) -> str:
    return "premium"

async def standard_path(ctx: dict) -> str:
    return "standard"
```

## How to build and run a graph workflow

```python
from oridecon.workflow import WorkflowBuilder, WorkflowEngine
from oridecon.workflow.graph.node import AbstractWorkflowNode, NodeType


class ValidateNode(AbstractWorkflowNode):
    name = "validate"
    node_type = NodeType.TASK

    async def execute(self, state: dict) -> dict:
        if "email" not in state:
            return {"valid": False}
        return {"valid": True}


class ProcessNode(AbstractWorkflowNode):
    name = "process"
    node_type = NodeType.TASK

    async def execute(self, state: dict) -> dict:
        return {"result": "processed"}


builder = WorkflowBuilder()
builder.add_node(ValidateNode())
builder.add_node(ProcessNode())
builder.add_edge("validate", "process")

engine = WorkflowEngine(builder.build())
result = await engine.execute("validate", initial_state={"email": "a@b.com"})
if result.is_ok():
    wf = result.unwrap()
    print(wf.final_state)
```

## How to define a saga with compensation

```python
from oridecon.result import Ok, Result
from oridecon.workflow import AbstractSaga
from oridecon.contracts.workflow import SagaStep, SagaStepError


class BookingSaga(AbstractSaga):
    VERSION = 1

    def __init__(self) -> None:
        super().__init__()
        self.add_step(SagaStep(
            name="book_flight",
            action=self._book_flight,
            compensation=self._cancel_flight,
        ))
        self.add_step(SagaStep(
            name="book_hotel",
            action=self._book_hotel,
            compensation=self._cancel_hotel,
        ))

    async def _book_flight(self) -> Result[None, SagaStepError]:
        return Ok(None)

    async def _cancel_flight(self) -> None:
        ...

    async def _book_hotel(self) -> Result[None, SagaStepError]:
        return Ok(None)

    async def _cancel_hotel(self) -> None:
        ...


saga = BookingSaga()
result = await saga.execute()
if result.is_ok():
    print("Booking complete")
```

## How to run a bulk operation

```python
from oridecon.workflow import BulkOperation
from oridecon.workflow.config import BulkOperationConfig


async def process_row(row: dict) -> dict:
    return {"id": row["id"], "status": "processed"}


config = BulkOperationConfig(batch_size=50, max_concurrency=10)
op = BulkOperation[dict, dict](processor=process_row, config=config)
result = await op.execute(items=[{"id": i} for i in range(200)])
if result.is_ok():
    batch = result.unwrap()
    print(f"Processed {len(batch.results)} items")
```

## How to use the state machine with persistence

```python
from oridecon.contracts.core.di import ContainerRegistrarProtocol
from oridecon.workflow.state import StateMachine
from oridecon.workflow.state.persistence import DatabaseStatePersistence


# Wire persistence in your provider
class MyProvider(Provider):
    async def register(self, container: ContainerRegistrarProtocol) -> None:
        from oridecon.contracts.data import DatabaseProviderProtocol
        db = await container.resolve(DatabaseProviderProtocol)

        persistence = DatabaseStatePersistence(
            provider=db,
            table_name="my_state_transitions",
        )
        container.singleton(StatePersistenceProtocol, lambda: persistence)
```

## How to use `@workflow` and `@saga_step` decorators

```python
from oridecon.workflow import workflow, saga_step


@workflow(name="onboarding", timeout=300.0, retries=1)
async def onboarding_workflow(ctx) -> None:
    ...


@saga_step(name="reserve_inventory", compensation=release_inventory)
async def reserve_inventory(ctx) -> None:
    ...
```

## How to handle saga version migration

```python
# Define a saga with a VERSION attribute
class MySaga(AbstractSaga):
    VERSION = 2  # Increment when step definitions change

# On resume, SagaVersionMismatchError is raised if versions differ
# Handle by migrating or restarting the saga instance
```

## How to configure graph checkpointing

```python
from oridecon.workflow.config import GraphConfig

config = GraphConfig(
    enabled=True,
    checkpoint_enabled=True,     # persist state for resumption
    max_iterations=50,
    node_timeout=30.0,
    total_timeout=600.0,
    parallel_branches=True,
    max_parallel_branches=5,
)
```
