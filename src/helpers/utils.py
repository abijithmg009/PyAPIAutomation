# Common Headers
def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers

def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic 99d92eb1ee40bc0=",
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers

# Read data from Excel, csv, json, YAML - Keep the fucntions in future