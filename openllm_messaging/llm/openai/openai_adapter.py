import logging

from openai import OpenAI

from openllm_messaging.llm.modelmessage import ModelMessage
from openllm_messaging.llm.modelmessage import Role


class OpenAIAdapter:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    async def text(self, messages: list[ModelMessage]) -> ModelMessage:
        """

        :param messages: A list of ModelMessages, containing a system prompt and a user prompt
        :return: the response message object
        """
        logging.info(f"Sending messages to OpenAI API: {messages}")
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[self._openai_api_format(message) for message in messages],
        )
        content = completion.choices[0].message.content
        total_tokens = completion.usage.total_tokens
        logging.info(f"Received raw response: {content}")
        return ModelMessage(content=content, tokens=total_tokens, role=Role.ASSISTANT)

    @staticmethod
    def _openai_api_format(message: ModelMessage) -> dict:
        """
        Transforms a ModelMessage object to a dictionary that can be sent to the OpenAI API.
        :param message: a single ModelMessage object to transform
        :return: the resulting dictionary
        """
        return {"content": message.content, "role": str(message.role.name.lower())}

    async def vision(self):
        # https://platform.openai.com/docs/guides/vision
        pass

    async def audio(self):
        # may have to use whisper until the gpt-4o API supports audio natively
        # https://platform.openai.com/docs/models/whisper
        pass
