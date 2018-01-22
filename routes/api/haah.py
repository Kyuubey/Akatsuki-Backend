from PIL import Image, ImageOps
from io import BytesIO

async def handle(req):
    im = Image.open(BytesIO(req.files[''].body))
    w, h = im.size
    im2 = ImageOps.mirror(im.crop((0, 0, w / 2, h)))
    
    im.paste(im2, (int(w / 2), 0))
    io = BytesIO()
    im.save(io, format='PNG')

    return req.Response(body=io.getvalue(), mime_type='image/png', encoding='UTF-8')

