from dns.resolver import Resolver, Answer
from threading import Thread


def resolve_address(hostname):
    res = Resolver('', False)
    res.nameservers = ['1.1.1.1']
    result = res.query(hostname)  # type: Answer
    for item in result.response.answer:
        if item.rdtype == 1:
            return item.items[0]


class ResolveThread(Thread):
    hostname = ""
    address = ""

    def __init__(self, hostname):
        Thread.__init__(self)
        self.hostname = hostname

    def run(self):
        self.address = str(resolve_address(self.hostname))
