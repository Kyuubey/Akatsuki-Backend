FROM python:alpine
WORKDIR /usr/src/backend
COPY . /usr/src/backend
RUN apk update && \
    apk add build-base freetype-dev jpeg-dev zlib-dev git
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install --user -r requirements.txt
CMD ["python3.6", "main.py"]
