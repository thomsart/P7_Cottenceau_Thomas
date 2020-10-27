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
    userInput = userInput.replace("'", " ")
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

    return words_for_API

################################################################################

def get_from_mediawiki_subject(subject):

    name_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch="+subject+"&format=json"
    name_url = requests.get(name_url)
    name_url = name_url.json()

    for key1, value1 in name_url.items():
        if key1 == "query":
            for key2, value2 in value1.items():
                if key2 == "search":
                    if value2 == []:
                        return False
                    else:
                        return True

################################################################################

def take_off_words(subject):

    content = subject.split()
    del content[0]
    subject02 = " ".join(content)

    return subject02

################################################################################

def get_from_mediawiki_good_name_subject(subject):
    """
    This methode allow to GET from the API MediaWiki information we needs.
    In this case we want the description of the research.
    """

    names =[]
    name_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch="+subject+"&format=json"
    name_url = requests.get(name_url)
    name_url = name_url.json()
    for key1, value1 in name_url.items():
        if key1 == "query":
            for key2, value2 in value1.items():
                if key2 == "search":
                    for el in value2:
                        for key3, value3 in el.items():
                            if key3 == 'title':
                                names.append(value3)

    name = names[0]

    return name

################################################################################

def get_from_mediawiki_article(name):
    """
    This methode allow to GET from the API MediaWiki information we needs.
    In this case we want the description of the research.
    """

    article = ""
    article_url = "https://fr.wikipedia.org/w/api.php?action=query&titles="+name+"&prop=extracts&exsentences=3&format=json&explaintext"
    article_url = requests.get(article_url)
    article_url = article_url.json()

    for key1, value1 in article_url.items():
        if key1 == "query":
            for key2, value2 in value1.items():
                if key2 == "pages":
                    for key3, value3 in value2.items():
                        for key4, value4 in value3.items():
                            if key4 == 'extract':
                                article += value4

    print(article)

    return article
    
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