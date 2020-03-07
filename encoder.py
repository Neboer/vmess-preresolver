import json
from base64 import b64encode


def encodeToRawSubscription(conf_dict):
    result_raw_string = ""
    for config in conf_dict:
        result_raw_string += "vmess://" + b64encode(json.dumps(config).encode('utf8')).decode('utf8') + "\n"
    return result_raw_string
