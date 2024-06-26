import pytest
from openai import OpenAI

from openllm_messaging.llm.openai.openai_adapter import OpenAIAdapter
from openllm_messaging.shared.model_message import Role


@pytest.fixture
def openai_adapter() -> OpenAIAdapter:
    adapter = OpenAIAdapter("some-token")
    adapter.client = OpenAI(api_key="some-token", base_url="http://localhost:5002/v1/")
    return adapter


def test_openai_adapter_chat_completion_simple(openai_adapter):
    response = openai_adapter.chat_completion_simple("Hello, world!")
    assert response.content == "Hello, world!"
    assert response.role == Role.ASSISTANT
