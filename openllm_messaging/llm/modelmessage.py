from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    SYSTEM = 0
    ASSISTANT = 1
    USER = 2


@dataclass
class ModelMessage:
    role: Role
    content: str
    tokens: int | None = None

    def as_dict(self):
        return {"role": self.role.name, "content": self.content, "tokens": self.tokens}
