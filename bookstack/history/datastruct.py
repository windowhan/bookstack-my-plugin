from dataclasses import dataclass
from datetime import *


@dataclass(order=True)
class HistoryStruct:
    id: int = 0
    bookId: int = 0
    name: str = ""
    slug: str = ""
    created_at: datetime = None
    updated_at: datetime = None
    is_completed: bool = False

