FROM python:3.11.5-alpine3.18
LABEL mantainer="sergiodnts828@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app /app
COPY scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /app/requirements.txt && \
  adduser --disabled-password --no-create-home dbuser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R dbuser:dbuser /venv && \
  chown -R dbuser:dbuser /data/web/static && \
  chown -R dbuser:dbuser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER dbuser

CMD ["commands.sh"]
