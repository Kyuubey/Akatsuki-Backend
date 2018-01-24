from PIL import Image, ImageOps
from io import BytesIO

async def handle(req):
    io = BytesIO()

    Image.open(BytesIO(req.files[''].body)).save(io, 'JPEG', quality=25)

    return req.Response(body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
