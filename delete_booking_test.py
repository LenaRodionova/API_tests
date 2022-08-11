import pytest

from helper_function import request_fun, decorator_to_create_booking, get_auth_token


@pytest.mark.smoke
@decorator_to_create_booking
def test_delete_booking(booking_id):
    auth_token = get_auth_token()
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    method = "DELETE"
    headers = {"Cookie": f"token={auth_token}"}
    r = request_fun(url=url, method=method, headers=headers)
    assert 300 > r.status_code >= 200
    print("status_code:", r.status_code)
    print("res_json:", r.text)
