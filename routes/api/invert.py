# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image, ImageOps


def handle(req):
    """POST"""
    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body)).convert('RGB')

    io = BytesIO()
    ImageOps.invert(im).save(io, format='PNG')

    return req.Response(
        body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
