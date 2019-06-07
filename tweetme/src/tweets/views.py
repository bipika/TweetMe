from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TweetModelForm
from .models import Tweet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

# Create your views here.


#Create
class TweetCreateView(FormUserNeededMixin,CreateView):
    # queryset = Tweet.objects.all()
    form_class=TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = "/tweet/create/"
    # success_url = reverse_lazy('tweet:list')
    # fields = ['user', 'content']
    login_url = '/admin/'


# def tweet_create_view(request):
#     form=TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance=form.save(commit=False)
#         instance.user= request.user
#         instance.save()
#     context={
#         "form":form
#     }
#     return render(request,'tweets/create_view.html',context)

#Retrieve
class TweetDetailView(DetailView):
    template_name="tweets/detail_view.html"
    queryset=Tweet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_object(self):
    #     print(self.kwargs)
    #     pk=self.kwargs.get("pk")
    #     print(pk )
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    # template_name="tweets/list_view.html"
    def get_queryset(self,*args,**kwargs):
        qs=Tweet.objects.all()
        print(self.request.GET)
        query=self.request.GET.get("q",None)
        if query is not None:
            qs= qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                          )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def tweet_detail_view(request,id=1):
#     obj= Tweet.objects.get(id=id)
#     print(obj)
#     context={
#         "objects":obj
#     }
#     return render(request,"tweets/detail_view.html",context)

# def tweet_list_view(request):
#     queryset=Tweet.objects.all()
#     print(queryset)
#     context={
#         "objects_list":queryset
#     }
#     return render(request,"tweets/list_view.html",context)

#Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = "/tweet/"

#Delete
class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('tweet:list')
    template_name = 'tweets/delete_confirm.html'