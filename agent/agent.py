from flask import Flask, Response
from logs.logs import Logs
from ports.ports import Ports
app = Flask(__name__)


@app.route("/logs/<imageid>")
def logs(imageid):
    l = Logs()
    cl = l.logsContainer(imageid)
    return(cl)


@app.route("/ports")
def ports():
    p = Ports()
    a = p.ports()
    return(a)

if __name__ == "__main__":
    app.run()
