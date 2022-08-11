import pytest

from helper_function import request_fun, decorator_to_create_booking


@pytest.mark.smoke
@decorator_to_create_booking
def test_get_booking_by_id(booking_id):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    r = request_fun(url=url)
    assert 300 > r.status_code >= 200
    print("status_code:", r.status_code)
    print("res_json:", r.json())
