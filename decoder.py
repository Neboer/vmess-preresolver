import base64
import json


def decodeToConfDict(message_string):
    message_string += "=" * (4 - len(message_string) % 4)
    result = base64.b64decode(message_string.encode('utf8')).decode('utf8').splitlines()
    decoded_conf_pool = []
    for vmesslink in result:
        conf_string = vmesslink[8:]
        decoded_conf_string = base64.b64decode(conf_string.encode('utf8')).decode('utf8')
        decoded_conf_object = json.loads(decoded_conf_string)
        decoded_conf_pool.append(decoded_conf_object)
    return decoded_conf_pool


if __name__ == '__main__':
    with open('neboer.txt', 'r', encoding='utf8') as neboer:
        good = neboer.read()
    result_dict = decodeToConfDict(good)
    print(result_dict)
