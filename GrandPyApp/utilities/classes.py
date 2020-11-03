#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request

import requests

from GrandPyApp.utilities import constants as cts


"""
In this module we have all the class methods we need to make the applicatin working.
The errors, the requests to the API, the treatements on the jsons or the inputs.
"""

################################################################################

class Errors():

    """
    We made this methode class in order to gather all potentials futur errors
    we could encounter.
    """

    @staticmethod
    def empty_input():

        """
        In this case of application the first reflex is to check if the user didn't
        tape entry with nothing inside the form. And if it's the case we return him
        an alert.
        """

        return cts.GRANDPY_ALLERT_1

    @staticmethod
    def unfound_subject():

        """
        If the request to mediawiki API gives nothing we alert the user that maybe
        he didn't wrote good is question. 
        """

        return cts.GRANDPY_ALLERT_2

################################################################################

class RequestMediaWiki():

    """
    We made this methode class to gather the requests on API.
    """

    @staticmethod
    def subject(subject):

        """
        This  static metode take a name or even a question in argument (a string one)
        and then send a request to the mediawiki in order to find something relevant.
        """

        article_url = "https://fr.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + subject + "&format=json"
        json_subject = requests.get(article_url)
        json_subject = json_subject.json()

        return json_subject

    @staticmethod
    def article(good_name):

        """
        Now that we have the good name for our research we can finally do the
        request to mediawiki to get the article and return it with this
        static metode.
        """

        article_url = "https://fr.wikipedia.org/w/api.php?action=query&titles=" + good_name + "&prop=extracts&exsentences=3&format=json&explaintext"
        json_article = requests.get(article_url)
        json_article = json_article.json()

        return json_article

################################################################################

class Json():

    """
    We gather all the methods on json object we create to make clear the script.
    """

    @staticmethod
    def check_if_subject(json_subject):

        """
        After we got a json in return of the method "subject()" from the
        RequestMediaWiki class the idea is to check if in the key named "search"
        there something. If it's not the case it means that maybe the orthograph
        of the research is not correct and in this case we return False and True
        if the "search" key contains something.
        """

        for key1, value1 in json_subject.items():
            if key1 == "query":
                for key2, value2 in value1.items():
                    if key2 == "search":
                        if value2 == []:
                            return False
                        else:
                            return True

    @staticmethod
    def get_good_name_subject(json_subject):
        
        """
        If the return of the function "check_if_subject()" in True it means that we
        have something relevant in our research and it's time to pick the correct
        name of our research in the value of the key named "Title" in order to have
        the good article the next time we'll request the mediawiki API with the
        methode "article()" of the "RequestMediaWiki" class.
        """

        names = []
        for key1, value1 in json_subject.items():
            if key1 == "query":
                for key2, value2 in value1.items():
                    if key2 == "search":
                        for el in value2:
                            for key3, value3 in el.items():
                                if key3 == 'title':
                                    names.append(value3)

        good_name = names[0]

        return good_name

    @staticmethod
    def take_n_cut_article(json_article):

        """
        Once we got the article we decide to cut it in order to don't charge to much
        our application with useless informations.
        """

        full_article = ""
        for key1, value1 in json_article.items():
            if key1 == "query":
                for key2, value2 in value1.items():
                    if key2 == "pages":
                        for key3, value3 in value2.items():
                            for key4, value4 in value3.items():
                                if key4 == 'extract':
                                    full_article += value4

        description =  ""
        for letter in full_article:
            if letter != "=":
                description += letter
            else:
                break

        return description

################################################################################

class Tools():

    """
    The idea here is to gather all the methods which allows us to do a
    treatment on strings object.
    """

    @staticmethod
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

    @staticmethod
    def take_off_words(subject):

        """
        Depending on the result of our first query to mediawiki we use this fonction
        to take-off words after words before each query to get something from
        mediawiki.
        """

        content = subject.split()

        if content == []:
            return ""
        else:
            del content[0]
            new_name_subject = " ".join(content)
            return new_name_subject

################################################################################