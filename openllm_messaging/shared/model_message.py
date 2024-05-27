from dataclasses import dataclass
from enum import Enum

TOKENS_PLACEHOLDER_VALUE = -1


class Role(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"


@dataclass
class ModelMessage:
    """
    A message that can be sent to or received from a model.
    Tracks token for pricing transparency and budgeting purposes. If a message is created by the user,
    the token count will default to None; if a message is created by the OpenAI API, the total_count will be used.
    More detailed scenarios can be implemented later on.
    """

    role: Role
    content: str
    tokens: int | None = None

    def as_dict(self):
        return {
            "role": self.role.value,
            "content": self.content,
            "tokens": TOKENS_PLACEHOLDER_VALUE if self.tokens is None else self.tokens,
        }
