# Read the CSV or EXCEL file
# Create a Function create_token which can take values from the Excel File
# Verify the Expected Result

# Read the Excel - openpyxl
import openpyxl
import requests
import pytest


from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json

# Step 1 Read the File and put the content into a [] array
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(APIConstants.url_create_token(), headers=common_headers_json(), json=payload)
    return response


def test_post_create_token():
    file_path = "/Users/abijithmg/PycharmProjects/PyAPIAutomation/tests/Data_driven_testing/testdata_ddt-2.xlsx"
    credentials = read_credentials_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        # Here you can also write the logic for negative and positive
        assert response.status_code == 200
        


