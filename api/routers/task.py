from fastapi import APIRouter

router = APIRouter()

import api.schemas.task as task_schema

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]


@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
#引数にリクエストボディ
async def create_task(task_body: task_schema.TaskCreate):
# dict に変換し、これらのkey/valueおよび id=1 を持つ task_schema.TaskCreateResponse インスタンスを作成
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())




@router.put("/tasks/{task_id}")
async def update_task():
    pass


@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
