#!/usr/bin/env python3.6

# Stdlib
from importlib.util import module_from_spec, spec_from_file_location
import mimetypes
import os

# External Libraries
from japronto import Application

app = Application()


class DynamicRoute:
    def __init__(self, dir_: str,
                 path: str):  # type: (DynamicRoute, str, str) -> None
        self.path = path[:-3]
        self.location = dir_ + path
        spec = spec_from_file_location(path[:-3].split(".")[-1], dir_ + path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        self.method = module.handle.__doc__
        del spec, module

    def run(self, req
            ):  # type: (DynamicRoute, japronto.Request) -> japronto.Response
        spec = spec_from_file_location(self.path[:-3].split(".")[-1],
                                       self.location)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        res = module.handle(req)
        del module, spec
        return res


def static_file(path: str):  # type: (str) -> (req: {Response}) -> Coroutine
    async def inner(req):  # type: ({Response}) -> Coroutine
        with open(path) as file:
            return req.Response(
                file.read(), mime_type=mimetypes.guess_type(path)[0])

    return inner


def find_static_files(dir_: str) -> list:  # type: (str) -> List[str]
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


def find_routes(dir_: str) -> list:  # type: (str) -> List[str]
    data = []
    for path, _, files in os.walk(dir_):
        if not files:
            continue

        for file in files:
            if not file.endswith(".py"):
                continue
            pathname = f"{path[len(dir_):]}/{file.strip()}"
            data.append(DynamicRoute(dir_, pathname))

    return data


routes = find_routes("routes")
static = find_static_files("static")

for route in routes:
    app.router.add_route(route.path, route.run, method=route.method)

for route, handle in static:
    app.router.add_route(route, handle, method="GET")

app.run(debug=True, port=int(os.environ.get('PORT', 5050)))
