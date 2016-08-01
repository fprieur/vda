from flask import Flask, Response
from docker import Client
app = Flask(__name__)

cli = Client(base_url='unix://var/run/docker.sock')


@app.route("/")
def hello():
    a = cli.logs("d10ebcd9a693",
                 stdout=True,
                 stream=True,
                 tail="all",
                 follow=True)

    def logs():
        for i in a:
            yield(i)
    return Response(logs(), mimetype='text/plain')


@app.route("/ports")
def ports():
    containers = cli.containers()
    cp = []
    for container in containers:
        cp.append(container['Ports'][0]['PublicPort'])
    return ' '.join(str(e) for e in cp)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
