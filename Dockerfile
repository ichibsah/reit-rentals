FROM python:3.9-slim-buster as stage-app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . code
WORKDIR /code
#RUN python manage.py runserver

#CMD ["gunicorn", "--config", "gunicorn.conf.py", "dentist:website"]

# Expose ports
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
#