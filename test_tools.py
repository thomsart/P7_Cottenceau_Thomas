#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

import pytest

from GrandPyApp.utilities import tools
from GrandPyApp.utilities import constants as cst


"""
In this module we have all the fonctions we need to make the applicatin working.
The treatements of the inputs and the query of API.
"""

################################################################################

def test_empty_input():

    assert tools.empty_input() == cst.GRANDPY_ALLERT_1

################################################################################

def test_unfound_subject():

    assert tools.unfound_subject() == cst.GRANDPY_ALLERT_2

################################################################################

def test_take_off_useless_words():

    assert tools.take_off_useless_words("TEST TEXT : .,;_!?") == "Test Text   "

################################################################################

class MockResponse():

    @staticmethod
    def json():
        return cst.JSON_TEST

def test_request_mediawiki_subject(monkeypatch):

    def mock_request(mock):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = tools.request_mediawiki_subject("test")

    assert mock_result["batchcomplete"] == ""

################################################################################

def test_check_if_subject():

    assert tools.check_if_subject(cst.JSON_TEST) == True

################################################################################

def test_take_off_words():

    assert tools.take_off_words("This is a Test") == "is a Test"

################################################################################

def test_get_good_name_subject():

    assert tools.get_good_name_subject(cst.JSON_TEST) == "Tour Eiffel"

################################################################################

def test_request_mediawiki_article(monkeypatch):

    def mock_request(mock):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = tools.request_mediawiki_article("test")

    assert mock_result["batchcomplete"] == ""

################################################################################

def test_take_n_cut_article():

    assert tools.take_n_cut_article(cst.JSON_ARTICLE) == cst.FINAL_ARTICLE
