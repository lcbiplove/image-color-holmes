FROM python:3.11-slim as builder

WORKDIR /color-finder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir ./wheels -r requirements.txt

FROM python:3.11-slim

WORKDIR /color-finder

RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /color-finder/wheels /wheels
COPY --from=builder /color-finder/requirements.txt .

RUN pip install --no-cache-dir /wheels/*

COPY . .

EXPOSE 5000

CMD ["gunicorn", "wsgi:main_app", "-b", "0.0.0.0:5000", "-w", "4", "--log-level", "debug"]
