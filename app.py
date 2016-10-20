#! /usr/bin/env python

import bottle
from bottle import abort, Bottle, static_file

PORT=8080
STATIC_ROOT='./static'
DEFAULT_INDEX='html/index.html'

app = Bottle()

@app.route('/')
def default_index():
	return static_file( DEFAULT_INDEX, root=STATIC_ROOT )

@app.route('/static/<filepath:path>')
def serve_static(filepath):
	return static_file( filepath, root=STATIC_ROOT )

if __name__ == '__main__':
	bottle.run(app, host='0.0.0.0', port=PORT)

