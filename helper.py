# -*- coding: utf-8 -*-
import os
import random
import string
import sys
from datetime import datetime
import psycopg2
from configparser import ConfigParser


appName = "sample01"

cur = os.getcwd()
data = cur + "/" + "database.ini"

def config(filename=data, section='postgresql'):
    parser = ConfigParser() # create a parser
    parser.read(filename) # read config file

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db