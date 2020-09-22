#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request

from . import app

from .utilities.tools import *


app.config.from_object('config')

@app.route('/')
def index():
    return render_template('layouts/default_GrandPy.html')

@app.route('/ajax', methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    result = take_off_useless_words(user_text)
    print("test => ",result)
    content = get_from_mediawiki(result)
    content = jsonify(content)

    return content


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
