FROM python:3.8

COPY ./warehouse/requirements.txt /

RUN pip install -r requirements.txt

COPY ./docker/warehouse/docker-entrypoint.sh ./docker/warehouse/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY ./warehouse/ /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
