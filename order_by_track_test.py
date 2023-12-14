import sender_request

# Проверка, что код ответа равен 200

def test_positive_assert_get_oder():
    response = sender_request.get_order_by_track()

    assert response.status_code == 200

