#coding: utf-8

import sys
sys.path.append("/home/hertogi/heimasida/")
import os
os.environ['PYTHONPATH'] = 'home/hertogi/heimasida/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'stigull.settings'

from pickle import load

from django.contrib.auth.models import User, Group
from django.core import serializers
from django.contrib.localflavor.is_.is_postalcodes import IS_POSTALCODES
from django.db import transaction

from scripts import load_objects
from user_profile.settings import controller
from stigull_profile.models import MATH_GROUP, PHYSICS_GROUP, FRESHMEN_GROUP, GOVERNMENT_GROUP, STIGULL_GROUP

UserProfile = controller.get_profile_model()
POSTALCODES = dict(IS_POSTALCODES)

@transaction.commit_on_success
def load_old_users():
    users = load_objects("auth.user.txt")
    groups = load_objects("./auth.group.txt")
    cities = load_objects("userarea.city.txt")
    postalcodes = load_objects("userarea.postalcode.txt")
    userinfo = load_objects("userarea.userinfo.txt")
    
    STIGULL = Group.objects.get(name = STIGULL_GROUP)
    MATH = Group.objects.get(name = MATH_GROUP)
    PHYSICS = Group.objects.get(name = PHYSICS_GROUP)
    FRESHMEN = Group.objects.get(name = FRESHMEN_GROUP)
    GOVERNMENT = Group.objects.get(name = GOVERNMENT_GROUP)
    
    for key, userinfo in userinfo.iteritems():
        fields = userinfo['fields']
    
        user_dict = users[fields['user']]['fields']
        user = User(username = user_dict['username'],
                    first_name = fields['first_name'],
                    last_name = fields['last_name'],
                    email = "%s@hi.is" % user_dict['username'],
                    is_active = user_dict['is_active'],
                    is_superuser = user_dict['is_superuser'],
                    is_staff = user_dict['is_staff'],
                    password = user_dict['password']
        )
        user.save()
        
    
        user_groups = [groups[id] for id in user_dict['groups'] ]
        for group in user_groups:
            groupname = group['fields']['name']
            if groupname == u"Stigull":
                user.groups.add(STIGULL)
            elif groupname == u"Nýnemar":
                user.groups.add(FRESHMEN)
            elif groupname == u"Stjórn":
                user.groups.add(GOVERNMENT)
                user.is_staff = True
        

        if fields['department'] == 1:
            user.groups.add(MATH)
        else:
            user.groups.add(PHYSICS)
            
    
        profile = user.get_profile()
        profile.kennitala = userinfo['pk']
        profile.middlenames = fields['middlenames']
        profile.gender = fields['gender']
        profile.gsm = fields['gsm']
        profile.phone = fields['phone']
        
        profile.homepages.create(url = "http://www.hi.is/~%s" % user_dict['username'], name = "Heimasvæði")
        
        try:
            profile.postalcode = postalcodes[fields['postalcode']]['fields']['postalcode']
            print profile.postalcode 
        except KeyError:
            pass
        profile.address = fields['address']
    
        profile.save()
        print profile
        print user
    
    



    