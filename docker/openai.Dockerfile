FROM weastur/poetry:1.8.3-python-3.12-slim

ENV OPENAI_API_KEY="SOME_KEY"
EXPOSE 5001

WORKDIR /app

# Copy relevant code
COPY openllm_messaging/llm/ ./openllm_messaging/llm/
COPY openllm_messaging/shared/ ./openllm_messaging/shared/
COPY openllm_messaging/openai_server.py ./openllm_messaging/openai_server.py

# Install dependencies
COPY pyproject.toml poetry.lock ./

# Required for Poetry
COPY README.md ./

RUN poetry install --with openai

CMD ["poetry", "run", "openai"]
