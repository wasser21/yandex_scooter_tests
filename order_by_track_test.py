import sender_request
import data

# Проверка, что код ответа равен 200

def test_positive_assert_get_oder():
    response_for_new_order = sender_request.post_new_order(data.order_body)
    track = sender_request.get_track(response_for_new_order)
    response = sender_request.get_order_by_track(track)
    print(response_for_new_order)
    print(track)
    print(response)
    assert response.status_code == 200

