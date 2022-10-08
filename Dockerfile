FROM python:3.10

ENV PYTHONPATH: "${PYTHONPATH}:../"

WORKDIR /

COPY . .

RUN chmod +x ./test.sh

CMD ["./test.sh"]