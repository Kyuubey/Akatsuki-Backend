from io import BytesIO
from PIL import Image, ImageDraw
import os, sys

def handle(req):
    """POST"""
    ship_im = Image.new('RGBA', (3072, 1024), (0, 0, 0, 0))
    path = os.path.dirname(os.path.realpath(sys.argv[0]))

    im = Image.open(BytesIO(req.files[list(req.files.keys())[0]].body)).convert("RGBA").resize((1024,1024), Image.ANTIALIAS)
    im2 = Image.open(f'{path}/public/img/heart.png').convert("RGBA").resize((1000, 1000), Image.ANTIALIAS)
    im3 = Image.open(BytesIO(req.files[list(req.files.keys())[1]].body)).convert("RGBA").resize((1024, 1024), Image.ANTIALIAS)

    ship_im.paste(im, (0, 0), im)
    ship_im.paste(im2, (1036, 12), im2)
    ship_im.paste(im3, (2048, 0), im3)

    io = BytesIO()
    ship_im.save(io, format='PNG')

    return req.Response(
            body=io.getvalue(), mime_type='image/png', encoding='UTF-8')
    
