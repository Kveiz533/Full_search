from PIL import Image
import sys
from io import BytesIO
from functions import get_ll
import requests


def get_picture(address, with_label=False):
    ll_span = get_ll(address)
    label = None
    if with_label:
        label = ll_span[0] + "," + "pm2dol"
    map_params = {
        "ll": ll_span[0], "spn": ll_span[1], "l": "map", "pt": label}
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(response.content)).show()


address = " ".join(sys.argv[1:])
get_picture(address, with_label=True)

