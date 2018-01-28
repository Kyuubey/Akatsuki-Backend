from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os, sys

async def handle(req):
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    font = ImageFont.truetype(f'{path}/public/fonts/comicsans.ttf', 40)

    txt = req.query['text']

    txt_img = Image.new('RGBA', (125, 60), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)

    im = Image.open(f'{path}/public/img/ilikethat.png')

    txt_draw.text((0, 0), txt, fill='black', font=font, anchor='center')

    im2 = txt_img.rotate(19, expand=1)

    im.paste(im2, (190, 160), im2)

    io = BytesIO()
    im.save(io, format='PNG')

    return req.Response(body=io.getvalue(), mime_type='image/png', encoding='UTF-8')

