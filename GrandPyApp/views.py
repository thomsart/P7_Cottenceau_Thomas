#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify


import config
from . import app
from .utilities.classes import *

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
        result = Tools.take_off_useless_words(user_text)
        subject = RequestMediaWiki.subject(result)
        name = Json.check_if_subject(subject)

        if name == True:
            good_name = Json.get_good_name_subject(subject)
            article = RequestMediaWiki.article(good_name)
            article = Json.take_n_cut_article(article)
            json = jsonify(article, result)
            return json

        else:
            while name == False:
                result = Tools.take_off_words(result)
                name = RequestMediaWiki.subject(result)
                name = Json.check_if_subject(name)

                if result != "" and name == True:
                    good_name = RequestMediaWiki.subject(result)
                    good_name = Json.get_good_name_subject(good_name)
                    article = RequestMediaWiki.article(good_name)
                    article = Json.take_n_cut_article(article)
                    json = jsonify(article, result)
                    return json

                elif result == "":
                    result = Errors.unfound_subject()
                    json = jsonify(result, result)
                    return json

    else:
        result = Errors.empty_input()
        json = jsonify(result, result)
        return json