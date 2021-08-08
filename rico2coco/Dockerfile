FROM python:3.9

WORKDIR /workspace

RUN pip install poetry && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock Makefile /workspace/

RUN make install

COPY . /workspace/

