FROM python:alpine

RUN pip install nltk

WORKDIR /app

COPY word_count.py /app/

COPY random_paragraphs.txt /app/

CMD python word_count.py

