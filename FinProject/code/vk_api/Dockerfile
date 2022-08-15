FROM python:3.8

COPY ./code /code
RUN pip install -r /code/requirements.txt

COPY ./code/mock.py ./code
WORKDIR /code

EXPOSE 5000

CMD ["python", "mock.py"]