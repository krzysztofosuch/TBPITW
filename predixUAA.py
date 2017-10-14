#!/bin/env python

import predix.admin.app
app = predix.admin.app.Manifest()

app.create_uaa('secret')
app.create_client('app_client_id', 'secret')

app.create_timeseries()
