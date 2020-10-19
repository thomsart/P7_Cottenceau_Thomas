#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from GrandPyApp.utilities import tools
from GrandPyApp.utilities import constants as cst


################################################################################

def test_take_off_useless_words():
    """
    The idea is to verify if what come out from this function is still what
    we want.
    """
    assert tools.take_off_useless_words("TESTING TEXT: D',De,Du;!?.") == "Testing Text d'dedu "

################################################################################

def test_get_from_mediawiki(monkeypatch):
    """
    Here we verify that the result of the request to wikimedia is still what
    we want.
    """  
    assert tools.get_from_mediawiki("Tour Eiffel ") == cst.FULL_ARTICLE

################################################################################

def test_cut_article():
    """
    We want to test if the function cut_article still gives the same result.
    """
    assert tools.cut_article(cst.FULL_ARTICLE) == cst.FINAL_ARTICLE

################################################################################

# def test_get_from_mediawiki(monkeypatch):
#     """
#     Here we verify that the result of the request to wikimedia is still what
#     we want.
#     """
#     result = cst.FULL_ARTICLE

#     def mockreturn(request):
#         return result

#     # monkeypatch.setattr()