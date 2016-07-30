FROM python:2.7-alpine
WORKDIR  /usr/app
COPY . /usr/app
RUN pip install -r /usr/app/requirements.txt
EXPOSE 5000
CMD [ "python", "/usr/app/agent.py" ]
