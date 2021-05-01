with open(r"C:\Users\Rodrigo Lima\Desktop\img.png", "rb") as image_file:
    import base64
    import requests
    import json
    from PIL import Image
    import io

    encoded_str = base64.b64encode(image_file.read())
    name = 'Bill'
    payload = dict(name=name, image=encoded_str.decode("utf-8"))
    response = requests.post('http://localhost:80/add-user', data=json.dumps(payload))
    print(json.loads(response.text))

    # encoded_str = str.encode(json.loads(response.text)['image'])
    
    # image_data = base64.b64decode(encoded_str)
    # image = Image.open(io.BytesIO(image_data))
    # image.show()        

# print('--------------------------------------------------------------')

# with open(r"C:\Users\Rodrigo Lima\Desktop\img2.png", "rb") as image_file:
#     import base64
#     import requests
#     import json
#     from PIL import Image
#     import io

#     encoded_str = base64.b64encode(image_file.read())

#     payload = dict(id=1, image=encoded_str.decode("utf-8"))
#     response = requests.patch('http://localhost:80/update-user-image', data=json.dumps(payload))
#     print(json.loads(response.text))

#     encoded_str = str.encode(json.loads(response.text)['image'])
    
#     image_data = base64.b64decode(encoded_str)
#     image = Image.open(io.BytesIO(image_data))
#     image.show()