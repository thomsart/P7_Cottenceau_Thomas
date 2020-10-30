#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request

import requests

from GrandPyApp.utilities import constants as cts


"""
In this module we have all the fonctions we need to make the applicatin working.
The treatements of the inputs and the query of API.
"""

################################################################################

def empty_input():

    """
    In this case of application the first reflex is to check if the user didn't
    tape entry with nothing inside the form. And if it's the case we return him
    an alert.
    """

    return """Tu ne me demande rien la mon petit ! Allez ne sois pas timide 
            je t'écoute..."""

################################################################################

def unfound_subject():

    """
    If the request to mediawiki API gives nothing we alert the user that maybe
    he didn't wrote good is question. 
    """

    return """Heuuu je suis desolé mon petit, mais la tu me poses une colle ! "
            Verifies si tu ne fais pas de faute dans ta question."""

################################################################################

def take_off_useless_words(userInput):

    """
    This methode is used to take-off all words or ponctuation we don't need to
    do our request to the API MediaWiki. It allow us to do a first clean of
    words which can be a problem in the query to the API.
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

    """
    This fonction send a first query to the API MediaWiki to verify if what we
    are searching exist with this way to write it. If not we'll take off some
    words with an other fonction untill we get something relevant. Indeed
    sometimes if you don't write properly the query of a subject you can get
    stranges results.
    """

    name_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + subject + "&format=json"
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

    """
    Depending the result of our first query to mediawiki we use this fonction to
    take-off words after words before each query to get something from mediawiki.
    """

    content = subject.split()
    del content[0]
    new_query = " ".join(content)

    return new_query

################################################################################

def get_from_mediawiki_good_name_subject(subject):

    """
    When we finally found the subject we take the good orthograph of it in the
    result(json) of the query to mediawiki.
    """

    names =[]
    name_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + subject + "&format=json"
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
    Now we get the good orthographe or way to send the query we use this function
    to get from MediaWiki information we needs. In our case the description of
    the subject.
    """

    article = ""
    article_url = "https://fr.wikipedia.org/w/api.php?action=query&titles=" + name + "&prop=extracts&exsentences=3&format=json&explaintext"
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

    return article
    
################################################################################

def cut_article(full_article):

    """
    We don't want to post the whole article which can be very long.
    """

    description =  ""
    for letter in full_article:
        if letter != "=":
            description += letter
        else:
            break

    return description
