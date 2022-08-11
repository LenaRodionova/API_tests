import pytest

from helper_function import *
import json


@pytest.mark.smoke
@decorator_to_create_and_delete_booking
def test_update_booking(booking_id):
    auth_token = get_auth_token()
    totalprice = random.randrange(100, 999)
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    method = "PUT"
    headers = {"Cookie": f"token={auth_token}", "Content-Type": "application/json"}
    data = {"firstname": "James", "lastname": "Kirk", "totalprice": totalprice, "depositpaid": True,
            "bookingdates": {"checkin": "2233-03-22", "checkout": "2371-01-01"}, "additionalneeds": "SC 937-0176 CEC"}
    r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
    assert 300 > r.status_code >= 200
    assert r.json()["firstname"] == data["firstname"]
    assert r.json()["lastname"] == data["lastname"]
    assert r.json()["totalprice"] == totalprice
    assert r.json()["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert r.json()["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]
    print("status_code:", r.status_code)
    print("res_json:", r.json())
