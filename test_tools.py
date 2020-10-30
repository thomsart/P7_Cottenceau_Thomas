#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from GrandPyApp.utilities import tools
from GrandPyApp.utilities import constants as cst


"""
In this module we have all the fonctions we need to make the applicatin working.
The treatements of the inputs and the query of API.
"""

################################################################################

def test_empty_input():

    assert tools.empty_input() == "Tu ne me demande rien la mon petit ! Allez ne sois pas timide je t'écoute..."

################################################################################

def test_unfound_subject():

    assert tools.unfound_subject() == "Heuuu je suis desolé mon petit, mais la tu me poses une colle ! Verifies si tu ne fais pas de faute dans ta question."

################################################################################

def test_take_off_useless_words():

    assert tools.take_off_useless_words("TEST TEXT : .,;_!?") == "Test Text   "

################################################################################

def test_get_from_mediawiki_subject():

    assert tools.get_from_mediawiki_subject("Paris") == True

################################################################################

def test_take_off_words():

    assert tools.take_off_words("This is a test") == "is a test"

################################################################################

def test_get_from_mediawiki_good_name_subject():

    assert tools.get_from_mediawiki_good_name_subject("paris") == "Paris"

################################################################################

def test_get_from_mediawiki_article():

    assert tools.get_from_mediawiki_article("Bougligny") == "Bougligny est une commune française située dans le département de Seine-et-Marne, en région Île-de-France.\nSes habitants sont appelés les Bouglignois. Au dernier recensement de 2017, la commune comptait 725 habitants."
 

################################################################################

def test_cut_article():

    assert tools.cut_article("This is a test == this part is supposed to be cut") == "This is a test "

################################################################################