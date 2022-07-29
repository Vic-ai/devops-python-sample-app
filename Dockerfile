FROM python:3.10.5
COPY . .
RUN pip install pipenv
RUN pipenv sync -d
CMD pipenv run python -m api
