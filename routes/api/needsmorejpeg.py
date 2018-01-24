from PIL import Image, ImageOps
from io import BytesIO

async def handle(req):
    io = BytesIO()

    im = Image.open(BytesIO(req.files[''].body))
    r,g,b,a = im.split()

    rgb_im = Image.merge("RGB", (r,g,b))

    rgb_im.save(io, 'JPEG', quality=1)

    return req.Response(body=io.getvalue(), mime_type='image/jpeg', encoding='UTF-8')
