from flask import Flask, Response
from docker import Client
from logs.logs import Logs
from ports.ports import Ports
app = Flask(__name__)

cli = Client(base_url='unix://var/run/docker.sock')


@app.route("/")
def logs():
    l = Logs()
    cl = l.logsContainer()
    return(cl)


@app.route("/ports")
def ports():
    p = Ports()
    a = p.ports()
    return(a)

if __name__ == "__main__":
    app.run()
