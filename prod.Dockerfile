FROM python:3.9.4-slim AS base

FROM base as builder
RUN apt-get update && apt-get install -y --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

FROM builder AS tester

COPY . /app
WORKDIR /app
RUN pytest

FROM base AS runner
COPY --from=tester /usr/local/lib/python3.9/ /usr/local/lib/python3.9/
COPY --from=tester /app /app

WORKDIR /app

ENTRYPOINT ["python", "-m", "spacechem-solver"]
USER 1001

LABEL name={NAME}
LABEL version={VERSION}