import datetime
import random

from conftest import RestfulBookerService


def decorator_to_create_booking(function_to_decorate):
    def wrapper():
        total_price = random.randrange(100, 999)
        date = datetime.date.today()

        data = {"firstname": "Test", "lastname": "User", "totalprice": total_price, "depositpaid": True,
                "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
                "additionalneeds": "No"}
        r = RestfulBookerService().create_booking(data=data)
        booking_id = r.json()["bookingid"]

        function_to_decorate(booking_id)

    return wrapper


def decorator_to_create_and_delete_booking(function_to_decorate):
    def wrapper():
        total_price = random.randrange(100, 999)
        date = datetime.date.today()

        data = {"firstname": "Test", "lastname": "User", "totalprice": total_price, "depositpaid": True,
                "bookingdates": {"checkin": f"{date}", "checkout": f"{date}"},
                "additionalneeds": "No"}
        r = RestfulBookerService().create_booking(data=data)
        booking_id = r.json()["bookingid"]

        function_to_decorate(booking_id)

        r = RestfulBookerService().delete_booking(booking_id=booking_id)

    return wrapper
