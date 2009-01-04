#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from news.feeds import LatestEntries
feeds = {
  'nyjustu-frettir': LatestEntries
}


urlpatterns = patterns('',

  url(r'^$','django.views.generic.simple.direct_to_template',
                kwargs = {'template': 'base.html'}, name = 'index'),
  (r'^vefstjorn/(.*)', admin.site.root),
  (r'^vefstjorn/skjolun/', include('django.contrib.admindocs.urls')),

  #(r'^athugasemdir/', include('django.contrib.comments.urls')),
  #(r'^athugasemdir/', include('comment_utils.urls')),

  #Students and phonebook
  (r'^nemendur/', include('user_profile.urls')),
  #(r'^simaskra/', include('phonebook.urls')),

    #(r'^frettir/', include('news.urls')),
  #(r'^upplysingar/log/', include('laws.urls')),
  #(r'^upplysingar/', include("student.urls")),

  #url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name="feeds"),

)