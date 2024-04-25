ARG VERION_NAME=python
FROM ${VERION_NAME}
COPY . /app
WORKDIR /app
RUN pip install nltk
RUN pip install gensim
CMD ["python","app.py"]
