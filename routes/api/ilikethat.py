from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from aiohttp import web

async def handle(req):
    font = ImageFont.truetype('./public/fonts/comicsans.ttf', 40)

    txt = req.query['text']

    txt_img = Image.new('RGBA', (125, 60), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)

    im = Image.open('./public/img/ilikethat.png')

    txt_draw.text((0, 0), txt, fill='black', font=font, anchor='center')

    im2 = txt_img.rotate(19, expand=1)

    im.paste(im2, (190, 160), im2)

    io = BytesIO()
    im.save(io, format='PNG')

    return web.Response(body=io.getvalue(), content_type='image/png', charset='UTF-8')

