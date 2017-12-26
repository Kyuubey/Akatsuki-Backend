from PIL import Image, ImageOps
from io import BytesIO
from aiohttp import web

async def handle(req):
    reader = await req.multipart()
    post_img = await reader.next()
    img_io = BytesIO()

    while True:
        chunk = await post_img.read_chunk()
        if not chunk:
            break
        img_io.write(chunk)

    im = Image.open(img_io)
    w, h = im.size
    im2 = ImageOps.flip(im.crop((0, 0, w, h / 2)))
    
    im.paste(im2, (0, int(h / 2)))
    io = BytesIO()
    im.save(io, format='PNG')

    return web.Response(body=io.getvalue(), content_type='image/png', charset='UTF-8')

