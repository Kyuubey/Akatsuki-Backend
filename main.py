#!/usr/bin/python3.6

from aiohttp import web

import os

#import routes.api.eyes
import routes.api.haah
import routes.api.hooh
import routes.api.ilikethat
import routes.api.waaw
import routes.api.woow

app = web.Application()
app.router.add_get('/api/ilikethat', routes.api.ilikethat.handle)
#app.router.add_post('/api/eyes', routes.api.eyes.handle)
app.router.add_post('/api/haah', routes.api.haah.handle)
app.router.add_post('/api/hooh', routes.api.hooh.handle)
app.router.add_post('/api/waaw', routes.api.waaw.handle)
app.router.add_post('/api/woow', routes.api.woow.handle)

web.run_app(app, port=int(os.environ.get('PORT')) if os.environ.get('PORT') else 5050)

