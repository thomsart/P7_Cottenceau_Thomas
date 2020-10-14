#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request


import config
from . import app
from .utilities.tools import *

################################################################################

app.config.from_object('config')

@app.route('/')
def index():
    gmap_api_key = config.GOOGLEMAP_API_KEY
    return render_template('layouts/default_GrandPy.html', gmap_api_key = gmap_api_key)

@app.route('/ajax', methods=["POST"])
def ajax():
    user_text = request.form["userText"]
    result = take_off_useless_words(user_text)
    print("test => ",result)
    article = get_from_mediawiki(result)
    article = cut_article(article)
    article = jsonify(article, result)
    
    return article
    
        
################################################################################