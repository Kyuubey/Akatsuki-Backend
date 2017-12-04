from io import BytesIO
from PIL import Image
from flask import Response

def handle(req):

    txt = req.args['text']

    im = Image.open('./public/img/ilikethat.png')
    io = BytesIO()
    im.save(io, format='PNG')

    return Response(io.getvalue(), mimetype='image/png')
