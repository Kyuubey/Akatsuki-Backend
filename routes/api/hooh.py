# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image, ImageOps


async def handle(req):
    """POST"""
    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body))
    w, h = im.size
    im2 = ImageOps.flip(im.crop((0, 0, w, h / 2)))

    im.paste(im2, (0, int(h / 2)))
    io = BytesIO()
    im.save(io, format='PNG')

    return req.Response(
        body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
