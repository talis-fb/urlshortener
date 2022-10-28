FROM python:3.10

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install

COPY . .

RUN pipenv install --system --deploy

CMD ["python", "manage.py", "runserver"]
