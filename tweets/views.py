from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixin import FormUserNeed,NotSameUser


# Create your views here.

class Tweetcreateview(LoginRequiredMixin,FormUserNeed, CreateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = "/tweets/"
    login_url = "/admin/"
    #
    #     # def form_valid(self, form):
    #     #     if self.request.user.is_authenticated:
    #     #         form.instance.user = self.request.user
    #     #         return super(Tweetcreateview, self).form_valid(form)
    #     #     else:
    #     #         return self.form_invalid()


class Tweetupdateview(LoginRequiredMixin,NotSameUser,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweets/"

class Tweetdeleteview(LoginRequiredMixin,DeleteView):
    model=Tweet
    form_class=TweetModelForm
    template_name='tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list")

class Tweetdetailview(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self ):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)


class Tweetlistview(LoginRequiredMixin,ListView):

    def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        print(self.request.GET)
        query=self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                    Q(content__icontains=query)|
                    Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context=super(Tweetlistview,self).get_context_data(*args, **kwargs)
        context["create_form"]=TweetModelForm()
        context["create_url"]=reverse_lazy("tweet:create")
        return context

    login_url = "/admin/"
    template_name = "tweets/list_view.html"

# def tweet_detail_view(request,id=2):
# 	obj=Tweet.objects.get(id=id)
# 	print(obj)
# 	params={
# 		"object":obj
# 	}
# 	return render(request,"tweets/detail_view.html",params)


# def tweet_list_view(request):
# 	queryset=Tweet.objects.all()

# 	params={
# 		"query":queryset
# 	}
# 	return render(request,"tweets/list_view.html",params)
