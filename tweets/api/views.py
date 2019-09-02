from rest_framework import generics
from .serializers import Tweetmodelserial
from ..models import Tweet
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class TweetlistApiview(generics.ListAPIView):
    # queryset = Tweet.objects.all()
    serializer_class = Tweetmodelserial

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

