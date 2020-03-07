from dns.resolver import Resolver, Answer
from threading import Thread


def resolve_address(hostname, nameserver):
    res = Resolver('', False)
    res.nameservers = [nameserver]
    result = res.query(hostname)  # type: Answer
    for item in result.response.answer:
        if item.rdtype == 1:
            return item.items[0]


class ResolveThread(Thread):
    hostname = ""
    address = ""
    nameserver = ""

    def __init__(self, hostname, nameserver):
        Thread.__init__(self)
        self.hostname = hostname
        self.nameserver = nameserver

    def run(self):
        self.address = str(resolve_address(self.hostname, self.nameserver))
