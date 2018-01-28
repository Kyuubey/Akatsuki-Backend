#!/usr/bin/env python3.6

# Stdlib
from importlib.util import module_from_spec, spec_from_file_location
import mimetypes
import os

# External Libraries
from japronto import Application

app = Application()


def static_file(path):
    async def inner(req):
        with open(path) as file:
            return req.Response(
                file.read(), mime_type=mimetypes.guess_type(path)[0])

    return inner


def find_static_files(dir_):
    data = []
    for path, _, files in os.walk(dir_):
        if not files:
            continue

        for file in files:
            if not file.split(".")[-1] not in ("html", "css", "js"):
                continue

            pathname = f"{path[len(dir_):]}/{file.strip()}"
            data.append(pathname.split(".")[0], static_file(pathname))

    return data


def find_routes(dir_):
    data = []
    for path, _, files in os.walk(dir_):
        if not files:
            continue

        for file in files:
            if not file.endswith(".py"):
                continue
            pathname = f"{path[len(dir_):]}/{file.strip()}"
            spec = spec_from_file_location(file.strip()[:-3], dir_ + pathname)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            data.append((pathname[:-3], module.handle))

    return data


routes = find_routes("routes")
static = find_static_files("static")

for route, handle in routes:
    app.router.add_route(route, handle, method=handle.__doc__.strip())

for route, handle in static:
    app.router.add_route(route, handle, method="GET")

app.run(debug=True, port=int(os.environ.get('PORT', 5050)))
