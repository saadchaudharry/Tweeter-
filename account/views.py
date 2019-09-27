from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

# Create your views here.
User=get_user_model()
class Userdetail(DetailView):
    template_name = 'userdetial.html'
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))