FROM python:3.10-slim


WORKDIR /

COPY ./bot /bot

RUN pip install --no-cache-dir -r /bot/requirements.txt

CMD ["python", "/bot/main.py"]