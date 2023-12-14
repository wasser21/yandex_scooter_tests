import configuration
import data
import requests

# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)

response = post_new_order(data.order_body)


# Сохранение номера трека заказа
def get_track():
    track_body = str(post_new_order(data.order_body).json()['track'])
    return track_body


# Получение заказа по номера трека заказа
def get_order_by_track():
    track = get_track()
    track_params = {"t": track}

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params=track_params)

