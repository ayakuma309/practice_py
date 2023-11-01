from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema

# 引数としてスキーマ task_create: task_schema.TaskCreate を受け取る。
async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    # task_model.Task に変換して、DB に保存する。
    task = task_model.Task(**task_create.dict())
    db.add(task)
    # DBにコミットする
    await db.commit()
    # DB上のデータを元にTaskインスタンス task を更新する。
    await db.refresh(task)
    return task
