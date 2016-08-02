from docker import Client

cli = Client(base_url='unix://var/run/docker.sock', version='1.20')


class Ports(object):
    def ports(self):
        containers = cli.containers()
        cp = []
        for container in containers:
            cp.append(container['Ports'][0]['PublicPort'])
        return ' '.join(str(e) for e in cp)
