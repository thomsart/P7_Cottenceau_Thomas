#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

import pytest

from GrandPyApp.utilities import classes as cl
from GrandPyApp.utilities import constants as cst


"""
In this module we have all the fonctions we need to make the applicatin working.
The treatements of the inputs and the query of API.
"""

################################################################################


def test_empty_input():

    assert cl.Errors.empty_input() == cst.GRANDPY_ALLERT_1


def test_unfound_subject():

    assert cl.Errors.unfound_subject() == cst.GRANDPY_ALLERT_2

################################################################################


class MockResponse():

    @staticmethod
    def json():
        return cst.JSON_TEST


def test_request_mediawiki_subject(monkeypatch):

    def mock_request(mock):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = cl.RequestMediaWiki.subject("test")

    assert mock_result["batchcomplete"] == ""


def test_request_mediawiki_article(monkeypatch):

    def mock_request(mock):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = cl.RequestMediaWiki.article("test")

    assert mock_result["batchcomplete"] == ""

################################################################################


def test_check_if_subject():

    assert cl.Json.check_if_subject(cst.JSON_TEST) == True


def test_get_good_name_subject():

    assert cl.Json.get_good_name_subject(cst.JSON_TEST) == "Tour Eiffel"


def test_take_n_cut_article():

    assert cl.Json.take_n_cut_article(cst.JSON_ARTICLE) == cst.FINAL_ARTICLE

################################################################################


def test_take_off_useless_words():

    assert cl.Tools.take_off_useless_words("TEST TEXT : .,;_!?") == "Test Text   "


def test_take_off_words():

    assert cl.Tools.take_off_words("This is a Test") == "is a Test"

################################################################################