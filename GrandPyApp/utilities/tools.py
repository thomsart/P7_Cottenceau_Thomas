#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request

import requests

from .constant import *


def take_off_useless_words(userInput):
    """This methode is used to take-off all words we don't need to do our
    request on the API MediaWiki"""

    try:
        userInput = str(userInput)
    except ValueError:
        print("Ce ne sont pas des mots")

    words_for_API = ""
    user_input = userInput.split(" ")
    for word in user_input:
        if word in stop_french_words:
            pass
        else:
            words_for_API += str(word) + " "

    words_for_API = words_for_API.replace("l'", "")
    words_for_API = words_for_API.title()
    words_for_API = words_for_API.replace("D'", "d'")
    words_for_API = words_for_API.replace("De", "de")
    words_for_API = words_for_API.replace("Du", "du")

    return words_for_API

###############################################################################

def get_from_mediawiki(subject):
    """This methode allow to GET from the API MediaWiki information we needs.
    In this case we want the description of the research."""

    url = "https://fr.wikipedia.org/w/api.php?action=query&titles="+subject+"&prop=extracts&exsentences=10&format=json&explaintext"
    answer = requests.get(url)
    answer = answer.json()
    text = ""
    for key1, value1 in answer.items():
        if key1 == "query":
            for key2, value2 in value1.items():
                if key2 == "pages":
                    for key3, value3 in value2.items():
                        for key4, value4 in value3.items():
                            if key4 == 'extract':
                                text += value4
    description = ""
    for letter in text:
        if letter != "=":
            description += letter
        else:
            break

    return description
    