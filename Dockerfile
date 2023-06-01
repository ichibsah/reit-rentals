FROM python:3.9-slim-buster as stage-app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . code
WORKDIR /code

# Expose ports
EXPOSE 8000

# Expose volumes
VOLUME ["/code"]

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
#