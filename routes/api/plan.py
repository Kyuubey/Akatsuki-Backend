from io import BytesIO
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont


def handle(req):
    """GET"""

    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    font = ImageFont.truetype(f'{path}/public/fonts/notosans.ttf', 50)

    def get_im(text):
        text = '\n'.join(textwrap.wrap(text, 10))

        img = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        img_draw = ImageDraw.Draw(img)

        w, h = img_draw.multiline_textsize(text, font=font)

        # w, h = font.getsize(text)

        font_size = int(100 / w * font.size)

        im_font = ImageFont.truetype(f'{path}/public/fonts/notosans.ttf',
                                     min(font_size, font.size))

        img_draw.multiline_text((0, 0), text, fill='black',
                                font=im_font, anchor='center')

        return img

    plan = Image.open(f'{path}/public/img/plan.png')

    step1 = req.query['step1']
    step2 = req.query['step2']
    step3 = req.query['step3']

    step1_im = get_im(step1)
    step2_im = get_im(step2)
    step3_im = get_im(step3)

    plan.paste(step1_im, (190, 60), step1_im)
    plan.paste(step2_im, (510, 60), step2_im)
    plan.paste(step3_im, (190, 280), step3_im)
    plan.paste(step3_im, (510, 280), step3_im)

    io = BytesIO()
    plan.save(io, format='PNG')

    return req.Response(
        body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
