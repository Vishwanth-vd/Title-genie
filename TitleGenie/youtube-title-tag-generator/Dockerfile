FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN mkdir -p /app/hf_cache


ENV HF_HOME=/app/hf_cache
ENV TRANSFORMERS_CACHE=/app/hf_cache

CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
