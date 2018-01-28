#!/usr/bin/env python3.6

# Stdlib
from importlib.util import module_from_spec, spec_from_file_location
import os

# External Libraries
from japronto import Application

app = Application()


def find_routes(dir_):
    data = []
    for path, _, files in os.walk(dir_):
        if not files:
            continue

        for file in files:
            pathname = f"{path[len(dir_):]}/{file.strip()}"
            spec = spec_from_file_location(file.strip()[:-3], dir_ + pathname)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            data.append((pathname[:-3], module.handle))

    return data


routes = find_routes("routes")

for route, handle in routes:
    app.router.add_route(route, handle, handle.__doc__)

app.run(debug=True, port=int(os.environ.get('PORT', 5050)))
