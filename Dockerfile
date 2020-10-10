FROM python:3.6

RUN pip install pipenv

ENV PROJECT_DIR /service

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

COPY . ${PROJECT_DIR}/

RUN pipenv install --system --deploy

CMD [ "pipenv", "run", "start" ]