from __future__ import absolute_import, unicode_literals

import twitter
from decouple import config
from .celery import app as celery_app

__all__ = ('celery_app',)

api = twitter.Api(consumer_key=config('CONSUMER_KEY'),
                  consumer_secret=config('CONSUMER_SECRET_KEY'),
                  access_token_key=config('ACCESS_TOKEN_KEY'),
                  access_token_secret=config('ACCESS_TOKEN_SECRET'))
