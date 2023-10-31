from typing import Optional

from pydantic import BaseModel, Field

# id, title, done の３フィールド
# それぞれint, Optional[str], bool の型ヒント
# Field はフィールドに関する付加情報
class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")
