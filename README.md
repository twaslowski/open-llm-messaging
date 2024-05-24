# openllm-messaging

This project aims to integrate LLMs such as GPT-4o into people's lives more easily by providing access to them
via different popular messaging apps such as Telegram, Discord, possibly the Meta messaging suite
(Messenger, Instagram) and possibly open source platforms such as RocketChat or Matrix.

## About

The goal of this project is to create a unified interface for interacting with LLMs such as GPT-4o
from different messaging apps. It will ensure consistent behaviour across different clients.

Different capabilities will be exposed via the interface, such as:

- Responding to texts
- Transcribing and responding to voice messages
- Receiving and responding to captioned images (e.g. "what's in this photo?")
- Summarizing voice messages
- Retrieving information from documents shared with the bot

Additionally, this solution gives the user the opportunity to add personalised data without exposing it to large
corporations. It also gives an increased measure of control, as options like a system prompt can be set.
Also, as the project expands, different LLMs can be added to the system, even allowing to integrate self-hosted
LLMs for a higher degree of privacy.

Overall, the main value proposition is this:

- **Integration**: Access to LLMs from different messaging apps
- **Consistency**: Same behaviour across different clients
- **Privacy**: No data is shared with large corporations

## Roadmap

I will build an initial prototype on Telegram, as I have experience in using the API, and it is a popular messaging app.
The prototype will be built using Python and the `python-telegram-bot` library and the GPT-4o model from OpenAI.

Afterward, I will expand the prototype to include other messaging apps. Initially, I will add Discord, as the
API is well-documented and integration should be relatively trivial. From here, I will extract the common capabilities
and create a middle layer that handles the interaction with the LLMs. This layer will allow eventual database
integration to retrieve relevant user data.

From there on, more messaging apps and LLMs can be added, as the general interface is defined. Ideally, I would
like to add the Meta messaging suite, as it is very popular, and other platforms such as Slack or RocketChat.
Gaining a user base will be crucial to gather user feedback as quickly as possible.

At the same time, the integration of LLMs will be expanded. Initially, I will use GPT-4o, but I would like to add
the option to use self-hosted LLMs relatively quickly to achieve the promised higher degree of privacy.