import pytest
import random

from conftest import RestfulBookerService
from helper_function import decorator_to_create_and_delete_booking


@pytest.mark.smoke
@decorator_to_create_and_delete_booking
def test_update_booking(booking_id):
    total_price = random.randrange(100, 999)
    data = {"firstname": "James", "lastname": "Kirk", "totalprice": total_price, "depositpaid": True,
            "bookingdates": {"checkin": "2233-03-22", "checkout": "2371-01-01"}, "additionalneeds": "SC 937-0176 CEC"}
    r = RestfulBookerService().update_booking(booking_id=booking_id, data=data)
    print("status_code:", r.status_code)
    print("res_json:", r.json())
    assert 200 <= r.status_code < 300
    assert r.json()["firstname"] == data["firstname"]
    assert r.json()["lastname"] == data["lastname"]
    assert r.json()["totalprice"] == total_price
    assert r.json()["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert r.json()["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
