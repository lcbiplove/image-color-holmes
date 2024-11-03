FROM python:3.11-alpine as builder

WORKDIR /color-finder

COPY requirements.txt . 

RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.11-alpine


WORKDIR /color-finder

COPY --from=builder /color-finder/wheels ./wheels
COPY --from=builder /color-finder/requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache ./wheels/*

EXPOSE 5000

CMD ["gunicorn", "wsgi:main_app", "-b", "0.0.0.0:5000", "-w", "4"]