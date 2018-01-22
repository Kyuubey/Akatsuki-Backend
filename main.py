#!/bin/env python3.6

from japronto import Application

import os

#import routes.api.eyes
import routes.api.haah
import routes.api.hooh
import routes.api.ilikethat
import routes.api.waaw
import routes.api.woow

app = Application()
app.router.add_route('/api/ilikethat', routes.api.ilikethat.handle, method="GET")
#app.router.add_post('/api/eyes', routes.api.eyes.handle)
app.router.add_route('/api/haah', routes.api.haah.handle, method="POST")
app.router.add_route('/api/hooh', routes.api.hooh.handle, method="POST")
app.router.add_route('/api/waaw', routes.api.waaw.handle, method="POST")
app.router.add_route('/api/woow', routes.api.woow.handle, method="POST")

app.run(debug=True, port=int(os.environ.get('PORT')) if os.environ.get('PORT') else 5050)

