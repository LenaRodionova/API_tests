import pytest

from helper_function import decorator_to_create_booking
from restful_booker_service import RestfulBookerService


@pytest.mark.smoke
@decorator_to_create_booking
def test_delete_booking(booking_id):
    r = RestfulBookerService().delete_booking(booking_id=booking_id)
    print("status_code:", r.status_code)
    print("res_json:", r.text)
    assert 200 <= r.status_code < 300
    assert r.text == "Created"
