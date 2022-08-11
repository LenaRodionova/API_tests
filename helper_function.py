import requests
import json
import datetime
import random


def request_fun(url, method="GET", data=None, headers=None):
    r = requests.request(url=url, method=method, data=data, headers=headers)
    print("REQUEST_URL", r.request.url)
    print("REQUEST_BODY", r.request.body)
    print("REQUEST_HEADERS", r.request.headers)
    return r


def get_auth_token():
    url = "https://restful-booker.herokuapp.com/auth"
    method = "POST"
    data = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}
    r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
    print("token", r.json()["token"])
    return r.json()["token"]


def decorator_to_create_booking(function_to_decorate):
    def wrapper():
        totalprice = random.randrange(100, 999)
        date = datetime.date.today()
        url = "https://restful-booker.herokuapp.com/booking"
        method = "POST"
        data = {"firstname": "Test", "lastname": "User", "totalprice": totalprice, "depositpaid": True,
                "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
                "additionalneeds": "No"}
        headers = {"Content-Type": "application/json"}
        r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
        booking_id = r.json()["bookingid"]

        function_to_decorate(booking_id)

    return wrapper


def decorator_to_create_and_delete_booking(function_to_decorate):
    def wrapper():
        totalprice = random.randrange(100, 999)
        date = datetime.date.today()
        auth_token = get_auth_token()

        url = "https://restful-booker.herokuapp.com/booking"
        method = "POST"
        data = {"firstname": "Test", "lastname": "User", "totalprice": totalprice, "depositpaid": True,
                "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
                "additionalneeds": "No"}
        headers = {"Content-Type": "application/json"}
        r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
        booking_id = r.json()["bookingid"]

        function_to_decorate(booking_id)

        url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        method = "DELETE"
        headers = {"Cookie": f"token={auth_token}"}
        r = request_fun(url=url, method=method, headers=headers)

    return wrapper
