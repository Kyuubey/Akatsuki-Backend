from PIL import Image, ImageOps
from io import BytesIO

async def handle(req):
    im = Image.open(BytesIO(req.files[''].body))

    io = BytesIO()
    ImageOps.flip(im).save(io, format='PNG')

    return req.Response(body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
