import pytest

from helper_function import request_fun
import json
import random
import datetime


@pytest.mark.smoke
def test_create_booking():
    totalprice = random.randrange(100, 999)
    date = datetime.date.today()
    url = "https://restful-booker.herokuapp.com/booking"
    method = "POST"
    data = {"firstname": "Test", "lastname": "User", "totalprice": totalprice, "depositpaid": True,
            "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
            "additionalneeds": "No"}
    headers = {"Content-Type": "application/json"}
    r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
    assert 300 > r.status_code >= 200
    assert r.json()["booking"]["firstname"] == data["firstname"]
    assert r.json()["booking"]["lastname"] == data["lastname"]
    assert r.json()["booking"]["totalprice"] == totalprice
    assert r.json()["booking"]["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert r.json()["booking"]["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
    print("status_code:", r.status_code)
    print("res_json:", r.json())
