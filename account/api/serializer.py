from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

user=get_user_model()

class Userdefault(serializers.ModelSerializer):
    follow_count =serializers.SerializerMethodField()
    url          =serializers.SerializerMethodField()
    class Meta:
        model=user
        fields=[
            "username",
            "first_name",
            "last_name",
            'follow_count',
            'url'
        ]
    def get_follow_count(self,obj):
        # print(obj.username)
        return 0
    def get_url(self,obj):
        return reverse_lazy("userD:userdetail",kwargs={"username":obj.username})