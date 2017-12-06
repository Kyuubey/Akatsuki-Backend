import cv2, numpy

from io import BytesIO
from PIL import Image, ImageDraw
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
    eye = Image.open('./public/img/eye.png')
    im_draw = ImageDraw.Draw(im)

    face_cascade = cv2.CascadeClassifier('./public/cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./public/cascades/haarcascade_eye.xml')
    arr = numpy.frombuffer(img_io.getbuffer(), numpy.uint8)
    cv_img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    gray_cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray_cv_img)
    eyes = eye_cascade.detectMultiScale(gray_cv_img)
    
    for (x, y, w, h) in eyes:
        eye_cp = eye.resize((w, h), Image.ANTIALIAS)
        im.paste(eye_cp, (int(x + (eye.width / w)), y), eye_cp)

    io = BytesIO()
    im.save(io, format='PNG')

    return web.Response(body=io.getvalue(), content_type='image/png', charset='UTF-8')

