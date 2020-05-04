from datetime import timedelta


CELERY_BEAT_SCHEDULE = {
    'get_top_tags_every_5s': {
       'task': 'get_top_tags',
       'schedule': timedelta(hours=6),
    },
}
