from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):

	class Meta:
		fields = ["text", "image"]
		model = Post


class ReplyTweetForm(forms.ModelForm):
    class Meta:
        exclude = ["user", "date"]
        model = Reply