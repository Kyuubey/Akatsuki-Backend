from PIL import Image, ImageOps
from io import BytesIO

async def handle(req):
    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body))
    r,g,b,a = im.split()
    rgb_im = Image.merge("RGB", (r,g,b))

    io = BytesIO()
    ImageOps.invert(rgb_im).save(io, format='PNG')

    return req.Response(body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
