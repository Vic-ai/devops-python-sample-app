from python:3.10.5

COPY . .

RUN pip install pipenv
# RUN pipenv lock -r > requirements.txt
# RUN pip install -r requirements.txt
RUN pipenv sync -d

CMD pipenv run python -m api