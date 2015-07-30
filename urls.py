#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from news.feeds import LatestEntries
feeds = {
  'nyjustu-frettir': LatestEntries
}

import stigull.setup


urlpatterns = patterns('',
    url(r'^$','django.views.generic.simple.direct_to_template',
                kwargs = {'template': 'base.html'}, name = 'index'),
    (r'^vefstjorn/(.*)', admin.site.root),
    (r'^vefstjorn/skjolun/', include('django.contrib.admindocs.urls')),


    #Students and phonebook
    (r'^nemendur/', include('user_profile.urls')),
    (r'^simaskra/', include('phonebook.urls')),

    #Comments:
    #Notum ekki thetta, ta geta bottar spammad
    (r'^athugasemdir/', include('comment_utils.urls')),
    (r'^athugasemdir/', include('django.contrib.comments.urls')),

    #News
    (r'^frettir/', include('news.urls')),

    #Events:
    (r'^atburdir/', include('events.urls')),

    #Discount
    (r'^afslaettir/', include('discount.urls')),

    #About
    (r'^upplysingar/log/', include('laws.urls')),
    (r'^upplysingar/', include("student.urls")),

    #Spam protection
    (r'ruslpostur/', include("spam.urls")),

    #Generic email sending,
    (r'tolvupostur/', include("emailer.urls")),

    #Calendar
    (r'dagatal/', include("htmlcalendar.urls")),

    #Thetta virkar ekki rett
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name="feeds"),
)
