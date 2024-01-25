import json

import requests
import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import os

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_booking_dynamic
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    def load_schema(self,  schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_json_schema(self):
        # URL, Headers, Payload,

        payload = payload_create_booking()
        print(payload)
        # payload.update({"firstname: "pramod","lastname:"dutta})
        # payload["firstname"] = "Pramod"
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        response_josn = response.json()

        file = os.getcwd()+"/schema.json"

        schema = self.load_schema(file)



        try:
            validate(instance=response_josn, schema=schema)
        except ValidationError as e:
            print(e.message)
