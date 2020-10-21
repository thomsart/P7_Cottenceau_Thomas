#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request

import requests

from GrandPyApp.utilities import constants as cts


################################################################################

def take_off_useless_words(userInput):
    """
    This methode is used to take-off all words we don't need to do our request
    on the API MediaWiki.
    """

    try:
        userInput = str(userInput)
    except ValueError:
        print("Ce ne sont pas des mots")

    userInput = userInput.lower()
    userInputClean = ""
    ponctuation = [".",",",";",":","_","!","?"]
    for el in userInput:
        if el in ponctuation:
            continue
        else:
            userInputClean += el

    userInputClean = userInputClean.split(" ")

    words_for_API = ""
    for word in userInputClean:
        if word in cts.stop_french_words:
            pass
        else:
            words_for_API += str(word) + " "

    words_for_API = words_for_API.title()
    words_for_API = words_for_API.replace("L'", "")
    words_for_API = words_for_API.replace("D'", "d'")
    words_for_API = words_for_API.replace("De", "de")
    words_for_API = words_for_API.replace("Du", "du")

    return words_for_API

################################################################################

def get_from_mediawiki(subject):
    """
    This methode allow to GET from the API MediaWiki information we needs.
    In this case we want the description of the research.
    """
    url_search = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=tour%20de%pise&format=json"
    url = "https://fr.wikipedia.org/w/api.php?action=query&titles="+subject+"&prop=extracts&exsentences=3&format=json&explaintext"
    answer = requests.get(url)
    answer = answer.json()
    full_article = ""
    for key1, value1 in answer.items():
        if key1 == "query":
            for key2, value2 in value1.items():
                if key2 == "pages":
                    for key3, value3 in value2.items():
                        for key4, value4 in value3.items():
                            if key4 == 'extract':
                                full_article += value4

    return full_article
    
################################################################################

def cut_article(full_article):
    """
    We want to cut the text that the request provides because it's too long.
    """

    description =  ""
    for letter in full_article:
        if letter != "=":
            description += letter
        else:
            break

    return description

################################################################################