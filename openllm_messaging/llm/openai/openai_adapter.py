import logging

from openai import OpenAI
from openllm_messaging.llm.message import Message


class OpenAIAdapter:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    async def text(self, messages: list[Message]) -> Message:
        logging.info(f"Sending messages to OpenAI API: {messages}")
        completion = self.client.chat.completions.create(  # type: ignore
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[message.asdict() for message in messages],
        )
        response = completion.choices[0].message.content
        logging.info(f"Received response: {response}")
        return response

    async def vision(self):
        # https://platform.openai.com/docs/guides/vision
        pass

    async def audio(self):
        # may have to use whisper until the gpt-4o API supports audio natively
        # https://platform.openai.com/docs/models/whisper
        pass
