from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from flask import Response

def handle(req):

    font = ImageFont.truetype('./public/fonts/comicsans.ttf', 40)

    txt = req.args['text']

    txt_img = Image.new('RGBA', (125, 60), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)

    im = Image.open('./public/img/ilikethat.png')

    txt_draw.text((0, 0), txt, fill='black', font=font, anchor='center')

    im2 = txt_img.rotate(19, expand=1)

    im.paste(im2, (175, 160), im2)

    io = BytesIO()
    im.save(io, format='PNG')

    return Response(io.getvalue(), mimetype='image/png')

