FROM python:3.11-slim

WORKDIR /color-finder

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "wsgi:main_app", "-b", "0.0.0.0:5000", "-w", "4"]