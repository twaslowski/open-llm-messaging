import pytest

from openllm_messaging.llm.model_message import (
    ModelMessage,
    Role,
    TOKENS_PLACEHOLDER_VALUE,
)


@pytest.fixture
def message():
    return ModelMessage(role=Role.SYSTEM, content="Hello, world!")


def test_tokens_is_none_for_manually_created_message(message):
    assert message.tokens is None


def test_tokens_is_placeholder_value_if_none(message):
    assert message.as_dict() == {
        "role": "system",
        "content": "Hello, world!",
        "tokens": TOKENS_PLACEHOLDER_VALUE,
    }


def test_as_dict_returns_correct_dict(message):
    message.tokens = 100
    assert message.as_dict() == {
        "role": "system",
        "content": "Hello, world!",
        "tokens": 100,
    }
