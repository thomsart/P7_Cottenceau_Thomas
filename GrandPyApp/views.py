#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify


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

    if user_text != "":
        result = take_off_useless_words(user_text)
        print("test => ",result)
        name = get_from_mediawiki_subject(result)

        if name == True:
            good_name = get_from_mediawiki_good_name_subject(result)
            article = get_from_mediawiki_article(good_name)
            print(article)
            article = cut_article(article)
            json = jsonify(article, result)
            return json

        else:
            while name == False:
                result = take_off_words(result)
                name = get_from_mediawiki_subject(result)

                if result != "" and name == True:
                    good_name = get_from_mediawiki_good_name_subject(result)
                    article = get_from_mediawiki_article(good_name)
                    article = cut_article(article)
                    json = jsonify(article, result)
                    return json

                elif result == "":
                    result = unfound_subject()
                    json = jsonify(result, result)
                    return json

    else:
        result = empty_input()
        json = jsonify(result, result)
        return json