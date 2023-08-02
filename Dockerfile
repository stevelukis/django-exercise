# Do not modify the base image
FROM python:3.8-buster


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]