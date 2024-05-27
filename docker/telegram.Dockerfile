FROM weastur/poetry:1.8.3-python-3.12-slim

ENV TELEGRAM_TOKEN="SOME_TOKEN"

WORKDIR /app

# Copy relevant code
COPY openllm_messaging/messaging/telegram_client.py ./openllm_messaging/messaging/telegram_client.py
COPY openllm_messaging/telegram_client.py ./openllm_messaging/telegram_client.py
COPY openllm_messaging/shared/ ./openllm_messaging/shared/

# Install dependencies
COPY pyproject.toml poetry.lock ./

# Required for Poetry
COPY README.md ./

# Create temporary directory to download media
RUN mkdir -p /app/tmp

RUN poetry install --with telegram

CMD ["poetry", "run", "telegram"]
