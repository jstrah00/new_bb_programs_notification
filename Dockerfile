FROM python:3.11-slim

RUN pip install pdm

WORKDIR /app

ENV PDM_USE_VENV=false

COPY pyproject.toml pdm.lock* ./

RUN pdm install --prod

COPY . .

CMD ["pdm", "run", "main.py"]
