#!/usr/bin/env python
from flask import Flask

def the_answer():
    return 42

app = Flask(__name__)

@app.route('/')
def index():
    return 'The answer is: {}'.format(the_answer())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
