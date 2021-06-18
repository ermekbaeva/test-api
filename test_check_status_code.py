import requests

def test_get_anything_for_check_status_code_200():
    response = requests.get("https://httpbin.org/anything")
    assert response.status_code == 200

def test_get_anything_for_check_content_type_equals_json():
    response = requests.get("https://httpbin.org/anything")
    assert response.headers['Content-Type'] == "application/json"

def test_get_anything_for_check_origin_in_body():
    response = requests.get("https://httpbin.org/anything")
    response_body = response.json()
    assert response_body["origin"]=="109.252.184.19"

def test_post_anything_for_check_status_code_200():
    response = requests.post("https://httpbin.org/post")
    assert response.status_code == 200

def test_put_anything_for_check_status_code_200():
    response = requests.put("https://httpbin.org/put")
    assert response.status_code == 200

def test_delete_anything_for_check_status_code_200():
    response = requests.delete("https://httpbin.org/delete")
    assert response.status_code == 200

def test_patch_anything_for_check_status_code_200():
    response = requests.patch("https://httpbin.org/delete")
    assert response.status_code == 200