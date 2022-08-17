import pytest

from helper_function import decorator_to_create_booking
from restful_booker_service import RestfulBookerService


@pytest.mark.smoke
@decorator_to_create_booking
def test_get_booking_by_id(booking_id):
    r = RestfulBookerService().get_booking_by_id(booking_id)
    print("status_code:", r.status_code)
    print("res_json:", r.json())
    assert 200 <= r.status_code < 300
