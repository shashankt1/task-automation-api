FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 5000

ENV PYTHONPATH=/app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]