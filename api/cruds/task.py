from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result

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



async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()
