import pytest
import requests
import json


def request_fun(url, method="GET", data=None, headers=None):
    r = requests.request(url=url, method=method, data=data, headers=headers)
    print("REQUEST_URL", r.request.url)
    print("REQUEST_BODY", r.request.body)
    print("REQUEST_HEADERS", r.request.headers)
    return r


@pytest.fixture(scope="module")
def check_endpoint():
    url = "https://restful-booker.herokuapp.com/ping"
    r = request_fun(url=url)
    assert r.status_code == 201


class RestfulBookerService:
    def __init__(self, booking_id=None):
        self.booking_id = booking_id
        self.auth_token = (self.create_auth_token(data={"username": "admin", "password": "password123"})).json()[
            "token"]

    def create_auth_token(self, data):
        data = data
        url = "https://restful-booker.herokuapp.com/auth"
        method = "POST"
        headers = {"Content-Type": "application/json"}
        r = request_fun(url=url, method=method, data=json.dumps(data),
                        headers=headers)
        return r

    def create_booking(self, data):
        data = data
        url = "https://restful-booker.herokuapp.com/booking"
        method = "POST"
        headers = {"Content-Type": "application/json"}
        r = request_fun(url=url, method=method, data=json.dumps(data),
                        headers=headers)
        return r

    def delete_booking(self, booking_id):
        url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        method = "DELETE"
        headers = {"Cookie": f"token={self.auth_token}"}
        r = request_fun(url=url, method=method,
                        headers=headers)
        return r

    def get_booking_by_id(self, booking_id):
        url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        r = request_fun(url=url)
        return r

    def update_booking(self, booking_id, data):
        data = data
        url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        method = "PUT"
        headers = {"Cookie": f"token={self.auth_token}", "Content-Type": "application/json"}
        r = request_fun(url=url, method=method, data=json.dumps(data),
                        headers=headers)
        return r
