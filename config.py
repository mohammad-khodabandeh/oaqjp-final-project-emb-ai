# -*- coding: ascii -*-
"""
General Config
==============

"""

class Config:
    """
    Default config
    """
    TESTING = False
    DEBUG = False


class TestConfig(Config):
    """
    Test config when running tests
    """
    TESTING = True
    DEBUG = True
