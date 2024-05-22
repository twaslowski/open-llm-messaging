from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    SYSTEM = 0
    ASSISTANT = 1
    USER = 2


@dataclass
class Message:
    role: Role
    content: str
    tokens: int
