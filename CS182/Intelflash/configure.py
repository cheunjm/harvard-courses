# -*- coding: utf-8 -*-

"""
© Copyright 2014. Joon Yang & Jaemin Cheun. All rights reserved.

Config file for database
"""

import os
from configobj import ConfigObj


home_path = os.path.expanduser("~")
ROOT = os.path.join(home_path, 'Desktop/flashcards')
if not os.path.isdir(ROOT):
    os.mkdir(ROOT)
db_path = os.path.join(ROOT, "flashcards.db")

class conf(object):
    """
    Reads the settings file, and creates it with false values if it doesn't exist and sets vals to false if file empty.
    Returns a dict with a boolean for conf.settings['csv']
    Assumes conf file is in hidden flashcards folder and is called 'defaults.conf'
    """
    def __init__(self):
        self.home_path = os.path.expanduser("~")
        self.path = os.path.join(ROOT, "settings.conf")
        self.file_exists = os.path.isfile(self.path)
        self.settings = dict()
        self.parse()
        self.clean()

    def parse(self):
        if self.file_exists:
            config = ConfigObj(self.path)
            try:
                csv = config['csv']
            except:
                csv = None
                self.file_exists = False
            self.settings['csv'] = csv
            
        if not self.file_exists:
            default = False
            config = ConfigObj()
            config.filename = self.path
            config['csv'] = default
            config.write()
            self.file_exists = True
            self.parse()

    def clean(self):
        settings = self.settings
        for keyword in settings:
            stop_words = "true false True False".split()
            value = settings[keyword]
            if value == 'true' or value == "True":
                settings[keyword] = True
            if value == 'false' or value == "False":
                settings[keyword] = False
