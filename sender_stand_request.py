# Константин Салов, 23-я когорта - Финальный проект, Инженер по тестированию плюс
import configuration
import requests
import data

# создание заказа
def create_order (body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                          json=body)

# получение заказа по его номеру
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

def test_order_creation_and_retrival():
    response = create_order(data.order_body)
    track_number = response.json()["track"]
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()

