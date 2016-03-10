from django import forms
from .models import UserProfile, User


class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('name', 'color', 'url', 'company', 'location', 'bio', 'picture', 'banner', 'background')


class UserProfileUserForm(forms.Form):

    name = forms.CharField(label='Change Username')


class FollowForm(forms.Form):
    def process(self, request, kwargs):
        request.user.profile.follows.add(UserProfile.objects.get(user__username=kwargs['page_slug']))


class UnfollowForm(forms.Form):
    def process(self, request, kwargs):
        request.user.profile.follows.remove(UserProfile.objects.get(user__username=kwargs['page_slug']))
