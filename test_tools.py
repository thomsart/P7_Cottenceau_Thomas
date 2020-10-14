#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from GrandPyApp.utilities import tools


################################################################################

def test_take_off_useless_words():
    """
    The idea is to verify if what come out from this function is still what
    we want.
    """
    assert tools.take_off_useless_words("testing text : D',De,Du") == "Testing Text : d',de,du "

################################################################################

def test_get_from_mediawiki(monkeypatch):
    """
    Here we verify that the result of the request to wikimedia is still what
    we want.
    """
    result = "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 5,9 millions de visiteurs en 2016. Depuis son ouverture au public, elle a accueilli plus de 300 millions de visiteurs.\nD’une hauteur de 312 mètres à l’origine, la tour Eiffel est restée le monument le plus élevé du monde pendant quarante ans. Le second niveau du troisième étage, appelé parfois quatrième étage, situé à 279,11 mètres, est la plus haute plateforme d'observation accessible au public de l'Union européenne et la deuxième plus haute d'Europe, derrière la tour Ostankino à Moscou culminant à 337 mètres. La hauteur de la tour a été plusieurs fois augmentée par l’installation de nombreuses antennes. Utilisée dans le passé pour de nombreuses expériences scientifiques, elle sert aujourd’hui d’émetteur de programmes radiophoniques et télévisés.\n\n\n== Présentation générale ==\n\nContestée par certains à l'origine, la tour Eiffel fut d'abord, à l'occasion de l'exposition universelle de 1889, la vitrine du savoir-faire technique français. Plébiscitée par le public dès sa présentation à l'exposition, elle a accueilli plus de 200 millions de visiteurs depuis son inauguration."

    def mockreturn(request):
        return result
    
    assert tools.get_from_mediawiki("Tour Eiffel ") == result

################################################################################