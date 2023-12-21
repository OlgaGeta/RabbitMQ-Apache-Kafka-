FROM python:3.7
# pika для доступа к rabbitmq
RUN pip install pika
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/consumer
# копируем файл
COPY consumer.py .
CMD [ "python", "consumer.py" ]
