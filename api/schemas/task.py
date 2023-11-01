from typing import Optional

from pydantic import BaseModel, Field

# 共通部分
class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

# passにする= 何もしない文
class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# 共通部分titleを除く
# id, title, done の３フィールド
# それぞれint, Optional[str], bool の型ヒント
# Field はフィールドに関する付加情報
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

# orm_mode はDBと接続する際に使用
# レスポンススキーマ TaskCreateResponse が、暗黙的にORMを受け取り、レスポンススキーマに変換することを意味
    class Config:
        orm_mode = True
