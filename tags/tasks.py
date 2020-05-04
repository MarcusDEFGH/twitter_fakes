from twitter_fakes import api
from tags.models import Tag
from tweets.models import Tweet
from users.models import User

from celery import task


@task(name='create_tag')
def create_tag(name):
    Tag.objects.get_or_create(name=name)


@task(name='get_top_tags')
def get_top_tags():
    trends = [trend for trend in api.GetTrendsWoeid(woeid='455819')
              if trend.volume]
    for trend in trends:
        create_tag.delay(name=trend.name)


@task(name='craete_tweet')
def create_tweet(user_id, text, tag_id):
    Tweet.get_or_create(user__id=user_id,
                        text=text,
                        tag__id=tag_id)


@task(name='get_users')
def read_tweets(tag):
    search_results = api.GetSearch(term=tag.name, count=100)
    for result in search_results:
        user = result.user
        obj, created = User.objects.get_or_create(
            username=user.screen_name,
            tweets=user.statuses_count,
            followers=user.followers_count,
            following=user.friends)
        create_tweet.delay(user_id=obj.id, text=result.text, tag_id=tag.id)


@task(name='monitor_tags')
def monitor_tags():
    active_tags = Tag.objects.filter(is_active=True)
    for tag in active_tags:
        read_tweets.delay(tag)
