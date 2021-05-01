import base64
import io
import json

from PIL import Image
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def create_test_image():
    buffer = io.BytesIO()
    image = Image.new('RGBA', size=(25,25), color=(0,0,0))
    image.save(buffer, 'png')
    buffer.name = 'test.png'
    buffer.seek(0)
    encoded_image = base64.b64encode(buffer.read())
    encoded_image = encoded_image.decode("utf-8") # Required for JSON dumps
    return encoded_image


def test_add_user_success():
    name = 'John'
    image = create_test_image()
    payload = dict(name=name, image=image)
    response = client.post('/add-user', data=json.dumps(payload))
    assert response.status_code == 200
    assert 'id' in response.json().keys()
    user_id = response.json().get('id')
    return user_id


def test_add_user_invalid_image():
    name = 'John'
    image = 'test-img'
    payload = dict(name=name, image=image)
    response = client.post('/add-user', data=json.dumps(payload))
    assert response.status_code == 422


def test_add_user_missing_name():
    name = ''
    image = create_test_image()
    payload = dict(name=name, image=image)
    response = client.post('/add-user', data=json.dumps(payload))
    assert response.status_code == 422


def test_add_user_missing_image():
    name = 'John'
    image = ''
    payload = dict(name=name, image=image)
    response = client.post('/add-user', data=json.dumps(payload))
    assert response.status_code == 422


def test_add_user_and_get_user_image_success():
    user_id = test_add_user_success()
    response = client.get(f'/get-user-image/{user_id}')
    assert response.status_code == 200
    assert 'image' in response.json().keys()
    assert 'name' in response.json().keys()


def test_get_user_image_not_found():
    user_id = 0
    response = client.get(f'/get-user-image/{user_id}')
    assert response.status_code == 404


def test_get_user_image_invalid_id():
    user_id = None
    response = client.get(f'/get-user-image/{user_id}')
    assert response.status_code == 422


def test_add_user_and_update_user_image_success():
    user_id = test_add_user_success()
    image = create_test_image()
    payload = dict(id=user_id, image=image)
    response = client.patch(f'/update-user-image', data=json.dumps(payload))
    assert response.status_code == 200
    assert 'image' in response.json().keys()
    assert 'id' in response.json().keys()
