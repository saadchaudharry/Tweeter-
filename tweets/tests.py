from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet
# Create your tests here.

user=get_user_model()

class Tweetmodelform(TestCase):
    def setUp(self):
       some_user = user.objects.create(username="safadadsmfksfkf")
    def test_tweet_user(self):
        obj= Tweet.objects.create(
            user=user.objects.first(),
            content="some random stuff"
        )
        self.assertTrue(obj.content=="some random stuff")
        self.assertTrue(obj.id==1)