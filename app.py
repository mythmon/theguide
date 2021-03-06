#!/usr/bin/env python
import os

from flask import Flask

PORT = int(os.environ.get('PORT', 8080))
app = Flask(__name__)

def the_answer():
    return 42

@app.route('/')
def index():
    return 'The answer is: {0}'.format(the_answer())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
