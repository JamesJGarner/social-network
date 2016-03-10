from django import forms
from .models import Message, Reply


class MessageForm(forms.ModelForm):
    class Meta:
        exclude = ["from_user", "date", "read"]
        model = Message


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ['user', 'date']
