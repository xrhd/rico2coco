FROM python:3.9

WORKDIR /workspace

COPY pyproject.toml poetry.lock Makefile /workspace/

RUN pip install poetry 

RUN poetry config virtualenvs.create false && make install

COPY . /workspace/

