from rest_framework import serializers
from django.contrib.auth import get_user_model

user=get_user_model()

class Userdefault(serializers.ModelSerializer):
    follow_count=serializers.SerializerMethodField()
    class Meta:
        model=user
        fields=[
            "username",
            "first_name",
            "last_name",
            'follow_count'
        ]
    def get_follow_count(self,obj):
        print(obj.username)
        return 0