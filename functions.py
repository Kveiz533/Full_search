import requests


def get_toponym(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        pass
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def get_ll(address):
    toponym = get_toponym(address)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ",".join([toponym_longitude, toponym_lattitude])

    env = toponym["boundedBy"]["Envelope"]
    x1, y1, = env['lowerCorner'].split()
    x2, y2, = env['upperCorner'].split()
    dx = abs(float(x1) - float(x2)) / 2
    dy = abs(float(y1) - float(y2)) / 2
    span = f"{dx},{dy}"
    return ll, span
