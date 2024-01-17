import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers_json


@pytest.fixture()
def create_token(self):
    payload = payload_create_token()
    response = post_requests(url=APIConstants.url_create_token(), auth=None, headers=common_headers_json(),
                             payload=payload_create_token(), in_json=False)
    print(response.json()['token'])
    token = response.json()['token']
    verify_http_status_code(response, 200)
    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture()
def create_booking(self):
    payload = payload_create_booking()
    print(payload)
    # payload.update({"firstname: "pramod","lastname:"dutta})
    # payload["firstname"] = "Pramod"
    print(payload)

    response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                             payload=payload, in_json=False)
    print(response)
    bookingid = response.json()["bookingid"]
    print(bookingid)
    verify_response_key_should_not_be_none(response.json()["bookingid"])
    verify_http_status_code(response, 200)
    return bookingid
