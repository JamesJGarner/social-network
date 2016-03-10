from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, DetailView, FormView, DeleteView
from .models import Post, Reply
from django.views.generic.edit import ModelFormMixin
from django.http import Http404
from .forms import PostForm, ReplyTweetForm
from datetime import datetime


class DetailPost(DetailView):
    model = Post


class ListPost(ListView):
    model = Post


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        PostForm = form.save(commit=False)
        PostForm.date = datetime.now()
        PostForm.user = user=self.request.user
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)


class DeletePost(DeleteView):
    model = Post
    success_url = '/'
    def get_object(self, queryset=None):
        obj = super(DeleteView, self).get_object()
        if not obj.user.id == self.request.user.id:
            raise Http404
        return obj


class ReplyView(CreateView):
    model = Reply
    form_class = ReplyTweetForm
    success_url = '/'

    def form_valid(self, form):
        ReplyTweetForm = form.save(commit=False)
        ReplyTweetForm.date = datetime.now()
        ReplyTweetForm.user = user=self.request.user
        self.object = form.save()
        return super(ModelFormMixin, self).form_valid(form)

