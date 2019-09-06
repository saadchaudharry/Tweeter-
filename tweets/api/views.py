from rest_framework import generics
from .serializers import Tweetmodelserial
from ..models import Tweet
from django.db.models import Q
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin


class TweetCreateApiview(generics.CreateAPIView):
    serializer_class = Tweetmodelserial
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetlistApiview(generics.ListAPIView):
    # queryset = Tweet.objects.all()
    serializer_class = Tweetmodelserial
    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by("-pk")
        # print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

