from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')


class Logs(object):
    def logsContainer(self, imageid):
        a = cli.logs(imageid,
                     stdout=True,
                     tail="all")
        return a
