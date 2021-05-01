import base64
import io
from PIL import Image, UnidentifiedImageError

def is_valid_image(image):
    """
    NAME
        is_valid_image
    DESCRIPTION
        This function identifies if an image in bytes format is valid
        by attempting to convert it into a PIL.Image object.
    INPUT
        image: bytes
            Image in bytes format to be converted to a PIL.Image object.
    OUTPUT
        is_valid: boolean
            If True, then the image is valid.
    """
    is_valid = True

    try:
        image_data = base64.b64decode(image)
        image = Image.open(io.BytesIO(image_data))
    except (base64.binascii.Error, UnidentifiedImageError) as e:
        is_valid = False
    return is_valid
