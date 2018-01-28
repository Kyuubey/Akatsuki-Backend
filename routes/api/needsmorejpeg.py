# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image


async def handle(req):
    """POST"""
    io = BytesIO()

    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body))
    r, g, b, _ = im.split()

    rgb_im = Image.merge("RGB", (r, g, b))

    rgb_im.save(io, 'JPEG', quality=1)

    return req.Response(
        body=io.getvalue(), mime_type='image/jpeg', encoding='UTF-8')
