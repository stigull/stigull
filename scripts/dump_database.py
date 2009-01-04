#! /usr/bin/env python
# -*- coding: utf8 -*-

import sys
sys.path.append("/home/hertogi/heimasida/")

import os
os.environ['PYTHONPATH'] = 'home/hertogi/heimasida/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'stigull.settings'

from pickle import dump

from django.contrib.auth.models import User, Group
from django.core import serializers

from stigull.userarea.models import UserInfo, City, Postalcode
from stigull.news.models import News, Change
from stigull.comments.models import Comment

def serialize(model):
	file = open(create_filename(model), "w")
	data = serializers.serialize('python', model.objects.all())
	dump(data, file)
	file.close
	
def create_filename(model):
    """
    Returns a filename from a django 'Model'
    
    Usage:  filename = create_filename(model)
    Pre:    model is a django Model
    Post:   filename is a filename unique for model
    """
    return "%s.txt" % model._meta

serialize(User)
serialize(UserInfo)
serialize(Postalcode)
serialize(City)
serialize(Group)
serialize(News)
serialize(Change)
serialize(Comment)
