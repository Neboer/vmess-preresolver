from decoder import decodeToConfDict
from resolv import ResolveThread
from encoder import encodeToRawSubscription
from sys import argv


def getData():
    with open(argv[1], 'r', encoding='utf8') as neboer:
        good = neboer.read()
    return good


rawResponse = getData()
conf_dict = decodeToConfDict(rawResponse)
Thread_pool = [ResolveThread(conf["add"], argv[2]) for conf in conf_dict]
[thread.start() for thread in Thread_pool]
[thread.join() for thread in Thread_pool]
for index, thread in enumerate(Thread_pool):
    conf_dict[index]["add"] = thread.address

print(encodeToRawSubscription(conf_dict))
