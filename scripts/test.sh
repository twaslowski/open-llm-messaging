#!/bin/bash

set -e

function cleanup {
  echo "cleaning up"
  docker stop openai-mock-server
}
trap 'cleanup' EXIT

echo "launching openai mock server"
docker run -d --rm \
  --name openai-mock-server \
  -p 5002:5002 \
  -e MOCK_TYPE=echo \
  tobiaswaslowski/openai-mock-server

echo "running tests"
if [ -d .venv ]; then
  echo "found existing virtual environment. activating ..."
  source .venv/bin/activate
else
  echo "no virtual environment found. assuming dependencies are available."
fi

poetry run coverage run --source openllm_messaging -m pytest
poetry run coverage html
poetry run coverage xml -o test/coverage.xml
poetry run coverage-badge -f -o test/coverage.svg
