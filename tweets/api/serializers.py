from rest_framework import serializers

from ..models import Tweet
from account.api.serializer import Userdefault


class Tweetmodelserial(serializers.ModelSerializer):
    user=Userdefault()
    class Meta:
        model=Tweet
        fields=[
            "user",
            "content"
        ]