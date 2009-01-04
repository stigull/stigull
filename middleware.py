#! /usr/bin/env python
# -*- coding: utf8 -*-

from django.conf import settings

import logging
import logging.handlers

LOG_FILENAME = getattr(settings, "LOG_FILENAME","")    

logger = logging.getLogger('stigull')
handler = logging.handlers.RotatingFileHandler(
              settings.LOG_FILENAME, backupCount=5)
logger.addHandler(handler)

class FileLoggingMiddleware(object):
    def process_exception(self, request, exception):
        logger.error(exception)
