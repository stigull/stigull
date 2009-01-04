#! /usr/bin/env python
# -*- coding: utf8 -*-

from pickle import dump, load

PATH = "/home/johannth/django-projects/stigull/scripts/data/"
    
def load_objects(filename):
    """
    Restores a dictionary of instances from a pickled file
    
    Usage:  objects = load_objects(filename)
    Pre:    filename is a filename of a file containing a pickled Django model
    Post:   objects is a dictionary whose keys are the primary keys of model and 
            values are the models
    """
    return dict([(object['pk'], object) for object in load(open(PATH + filename)) ])


