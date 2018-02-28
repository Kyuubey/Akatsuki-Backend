import os
import sys
import requests

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def handle(req):
    """GET"""

    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    font = ImageFont.truetype(f'{path}/public/fonts/notosans.ttf', 40)

    txt = req.query['text']

    w, h = font.getsize(txt)

    font_size = int(1150 / w * font.size)
    font = ImageFont.truetype(f'{path}/public/fonts/notosans.ttf', min(font_size, font.size))

    txt_im = Image.new('RGB', (1200, 750), (255, 255, 255))
    im_draw = ImageDraw.Draw(txt_im)

    im = Image.open(f'{path}/public/img/floor.png')
    im_draw.text((10, 20), txt, fill='black', font=font, anchor='center')

    txt_im.paste(im, (0, 100))

    if 'image' in req.query:
        res = requests.get(req.query['image'])
        orig_im = Image.open(BytesIO(res.content)).convert('RGBA')

        head_im = orig_im.resize((50, 50))
        txt_im.paste(head_im, (195, 100), head_im)

        head2_im = orig_im.resize((100, 100))

        txt_im.paste(head2_im, (850, 100), head2_im)

        res.close()

    io = BytesIO()
    txt_im.save(io, format='PNG')

    return req.Response(
        body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
