#!/usr/bin/python3.6

from aiohttp import web

import routes.api.ilikethat, routes.api.eyes

app = web.Application()
app.router.add_get('/api/ilikethat', routes.api.ilikethat.handle)
app.router.add_post('/api/eyes', routes.api.eyes.handle)

web.run_app(app, port=5050)

