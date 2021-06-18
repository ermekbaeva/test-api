import requests

def test_get_anything_for_check_status_code_200():
    response = requests.get("https://httpbin.org/anything")
    assert response.status_code == 200

