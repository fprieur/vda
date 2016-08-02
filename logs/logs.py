from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')


class Logs(object):
    def logsContainer(self):
        a = cli.logs("d10ebcd9a693",
                     stdout=True,
                     tail="all",
                     follow=True)
        return a
