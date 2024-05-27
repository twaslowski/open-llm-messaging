import logging

from openai import OpenAI

from openllm_messaging.shared.model_message import ModelMessage
from openllm_messaging.shared.model_message import Role


class OpenAIAdapter:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def chat_completion_simple(self, prompt: str) -> ModelMessage:
        """
        Helper function for prototyping. Instead of having to go through the process of creating a
        list of ModelMessages with a System Prompt, this provides a simple way to get a response.
        :param prompt: a simple prompt.
        :return: The model response as a ModelMessage.
        """
        system_prompt = ModelMessage(
            content="You are a useful assistant.", role=Role.SYSTEM
        )
        user_prompt = ModelMessage(content=prompt, role=Role.USER)
        return self.chat_completion([system_prompt, user_prompt])

    def chat_completion(self, messages: list[ModelMessage]) -> ModelMessage:
        """
        :param messages: A list of ModelMessages, containing a system prompt and a user prompt
        :return: the response message object
        """
        logging.info(f"Sending messages to OpenAI API: {messages}")
        completion = self.client.chat.completions.create(
            model="gpt-4o",
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
        return {"content": message.content, "role": str(message.role.value)}

    def vision(self, image: str, prompt: str):
        """
        Multi-modal completion using the OpenAI API.
        :param image: base64-encoded image
        :param prompt: prompt to send to the model to get information about the image
        :return:
        """
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"{prompt}"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image}"  # noqa
                            },
                        },
                    ],
                }
            ],
            max_tokens=100,
        )
        content = completion.choices[0].message.content
        total_tokens = completion.usage.total_tokens
        logging.info(f"Received raw response: {content}")
        return ModelMessage(content=content, tokens=total_tokens, role=Role.ASSISTANT)

    async def audio(self):
        # may have to use whisper until the gpt-4o API supports audio natively
        # https://platform.openai.com/docs/models/whisper
        pass
