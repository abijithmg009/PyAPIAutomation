# to use the api constatnts

from src.constants.api_constants import base_url, APIConstants, BASE_url

def test_crud():
    print(BASE_url)

    url_function = base_url()
    print(url_function)

    url_class = APIConstants.base_url()
    print(url_class)