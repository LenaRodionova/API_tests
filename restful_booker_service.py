from helper_function import request_fun, get_auth_token
import json


class RestfulBookerService:
    def __init__(self, booking_id=None):
        self.url = None
        self.method = None
        self.data = None
        self.headers = None
        self.booking_id = booking_id
        self.auth_token = get_auth_token()

    def create_auth_token(self, data):
        self.data = data
        self.url = "https://restful-booker.herokuapp.com/auth"
        self.method = "POST"
        self.headers = {"Content-Type": "application/json"}
        r = request_fun(url=self.url, method=self.method, data=json.dumps(self.data),
                        headers=self.headers)
        return r

    def create_booking(self, data):
        self.data = data
        self.url = "https://restful-booker.herokuapp.com/booking"
        self.method = "POST"
        self.headers = {"Content-Type": "application/json"}
        r = request_fun(url=self.url, method=self.method, data=json.dumps(self.data),
                        headers=self.headers)
        return r

    def delete_booking(self, booking_id):
        self.url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        self.method = "DELETE"
        self.headers = {"Cookie": f"token={self.auth_token}"}
        r = request_fun(url=self.url, method=self.method, data=json.dumps(self.data),
                        headers=self.headers)
        return r

    def get_booking_by_id(self, booking_id):
        self.url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        r = request_fun(url=self.url)
        return r

    def update_booking(self, booking_id, data):
        self.data = data
        self.url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
        self.method = "PUT"
        self.headers = {"Cookie": f"token={self.auth_token}", "Content-Type": "application/json"}
        r = request_fun(url=self.url, method=self.method, data=json.dumps(self.data),
                        headers=self.headers)
        return r
