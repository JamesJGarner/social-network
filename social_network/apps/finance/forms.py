from django import forms
from .models import GiftCard
from social_network.apps.userprofiles.models import UserProfile


class GiftCardCheck(forms.ModelForm):
    giftcode = forms.CharField(label='Your code', max_length=16,)
    class Meta:
        model = GiftCard
        exclude = ['worth', 'expires', 'used', 'code']

        #TODO remove all fields exclude=[]


#TODO rename to something more meaningful
class RankChanger(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rank']

