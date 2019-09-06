from rest_framework import serializers

from ..models import Tweet
from account.api.serializer import Userdefault


class Tweetmodelserial(serializers.ModelSerializer):
    user=Userdefault(read_only=True)
    datedisplay=serializers.SerializerMethodField()

    class Meta:
        model=Tweet
        fields=[
            "user",
            "content",
            "timestamp",
            "datedisplay",
        ]

    def get_datedisplay(self,obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")