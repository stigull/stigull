#! /usr/bin/env python
# -*- coding: utf8 -*-

import scripts

from django.db import transaction
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatewords_html

from utils import slugify
from news.models import Entry, Content, EntryChange

def load_news():
	"""
	Restores the news from the old Stigull database
	
	Usage:  load_news()
	Pre:    None
	Post:   The batch of old news have been inserted into the new database
	""" 
	users = scripts.load_objects("auth.user.txt")
	news = scripts.load_objects("news.txt")
	changes = scripts.load_objects("change.txt")
	comments = scripts.load_objects("comments.txt")
	
	print users, news, changes, comments
	
	for pk, entry_dict in news.itervalues():
		#Zero or more news from news have been traversed
		#Each entry has the following fields 
		#   title, titleEn, body, bodyEn, datetimeCreated, author, changes, comments
		#For each entry a new Entry has been created with two 'Content' objects
		user = User.objects.get(username = users[news['author']].username)
		
		body_html = markdown(entry_dict['body'])
		body_en_html = markdown(entry_dict['bodyEn'])
		excerpt = truncatewords_html(body_html, 30)
		
		entry = Entry(publish_date = entry_dict['datetimeCreated'],
						author = user,
						enable_comments = True,
						status = Entry.LIVE_STATUS,
						slug = slugify(entry_dict['title']),
						excerpt = excerpt      
					)
					
		content_is = Content(entry = entry,
								language = 'is',
								title = entry_dict['title'],
								body = entry_dict['body'],
								body_html = body_html)
							
        content_en = Content(entry = entry,
                                language = 'en',
                                title = entry_dict['titleEn'],
                                body = entry_dict['bodyEn'],
                                body_html = body_en_html)
                                
        
		
	
	
	
	
load_news = transaction.commit_on_success(load_news)
	
