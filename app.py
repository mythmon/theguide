#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

def the_answer():
    return 42

@app.route('/')
def index():
    return 'The answer is: {0}'.format(the_answer())

if __name__ == '__main__':
    app.run(debug=True)
