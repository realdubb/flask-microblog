#!flask/bin/python3

import os
from app import app

# Configured for running in cloud 9

app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))