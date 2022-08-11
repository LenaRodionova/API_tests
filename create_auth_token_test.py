import pytest

from helper_function import request_fun
import json


@pytest.mark.smoke
def test_create_auth_token():
    url = "https://restful-booker.herokuapp.com/auth"
    method = "POST"
    data = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}
    r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
    assert 300 > r.status_code >= 200
    print("status_code:", r.status_code)
    print("res_json:", r.json())


@pytest.mark.parametrize("data", [{"username": "admin", "password": "password"},
                                  {"username": "admin123", "password": "password123"}])
def test_create_auth_token_fail(data):
    url = "https://restful-booker.herokuapp.com/auth"
    method = "POST"
    data = data
    headers = {"Content-Type": "application/json"}
    r = request_fun(url=url, method=method, data=json.dumps(data), headers=headers)
    assert 300 > r.status_code >= 200
    assert r.json()["reason"] == "Bad credentials"
    print("status_code:", r.status_code)
    print("res_json:", r.json())

