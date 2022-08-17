import pytest
import random
import datetime

from conftest import RestfulBookerService


@pytest.mark.smoke
def test_create_booking():
    total_price = random.randrange(100, 999)
    date = datetime.date.today()
    data = {"firstname": "Test", "lastname": "User", "totalprice": total_price, "depositpaid": True,
            "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
            "additionalneeds": "No"}
    r = RestfulBookerService().create_booking(data=data)
    print("status_code:", r.status_code)
    print("res_json:", r.json())
    assert 200 <= r.status_code < 300
    assert r.json()["booking"]["firstname"] == data["firstname"]
    assert r.json()["booking"]["lastname"] == data["lastname"]
    assert r.json()["booking"]["totalprice"] == total_price
    assert r.json()["booking"]["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert r.json()["booking"]["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
