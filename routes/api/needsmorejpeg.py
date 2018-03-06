# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image


def handle(req):
    """POST"""
    io = BytesIO()

    im = Image.open(
            BytesIO(req.files[list(req.files.keys())[0]].body)).convert('RGB')

    # if im.mode == 'RGBA':
    #     r, g, b, _ = im.split()
    #     Image.merge("RGB", (r, g, b)).save(io, 'JPEG', quality=1)
    # else:
    im.save(io, 'JPEG', quality=1)

    return req.Response(
        body=io.getvalue(), mime_type='image/jpeg', encoding='UTF-8')
