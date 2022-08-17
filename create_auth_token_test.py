import pytest
from restful_booker_service import RestfulBookerService


class TestCreateAuthToken:
    @pytest.mark.smoke
    def test_create_auth_token(self):
        data = {"username": "admin", "password": "password123"}
        r = RestfulBookerService().create_auth_token(data=data)
        print("status_code:", r.status_code)
        print("res_json:", r.json())
        assert 200 <= r.status_code < 300

    @pytest.mark.parametrize("data", [{"username": "admin", "password": "password"},
                                      {"username": "admin123", "password": "password123"}])
    def test_create_auth_token_fail(self, data):
        data = data
        r = RestfulBookerService().create_auth_token(data=data)
        print("status_code:", r.status_code)
        print("res_json:", r.json())
        assert 200 <= r.status_code < 300
        assert r.json()["reason"] == "Bad credentials"
