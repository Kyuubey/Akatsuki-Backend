# Stdlib
from io import BytesIO

# External Libraries
from PIL import Image
from aiohttp import web
import cv2
import numpy


async def handle(req):
    """POST"""
    reader = await req.multipart()
    post_img = await reader.next()
    img_io = BytesIO()

    while True:
        chunk = await post_img.read_chunk()
        if not chunk:
            break
        img_io.write(chunk)

    img = Image.open(img_io)
    eye = Image.open('./public/img/eye.png')

    eye_cascade = cv2.CascadeClassifier(
        './public/cascades/haarcascade_eye.xml')
    arr = numpy.frombuffer(img_io.getbuffer(), numpy.uint8)
    cv_img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    gray_cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray_cv_img)
    eyes = eye_cascade.detectMultiScale(gray_cv_img)

    for (x, y, w, h) in eyes:
        eye_cp = eye.resize((w, h), Image.ANTIALIAS)
        img.paste(eye_cp, (int(x + (eye.width / w)), y), eye_cp)

    io = BytesIO()
    img.save(io, format='PNG')

    return web.Response(
        body=io.getvalue(), content_type='image/png', charset='UTF-8')
