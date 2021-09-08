from dataclasses import dataclass

@dataclass(frozen=True)
class BookStackToken:
    name: str = ""
    tid: str = ""
    secret: str = ""
    host: str = ""
