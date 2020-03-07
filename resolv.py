from dns.resolver import Resolver, Answer
from threading import Thread
from re import match


# 这里的域名解析，预先带有一个ip检查功能。如果输入的域名就是ip地址，解析会直接返回。
def checkIfIpAddress(check_str):
    result = match(
        r"(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",
        check_str)
    return result is not None


def resolve_address(hostname, nameserver):
    if checkIfIpAddress(hostname):
        return hostname
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
