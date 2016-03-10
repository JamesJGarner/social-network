from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import GiftCardCheck, RankChanger
from .models import GiftCard
from social_network.apps.userprofiles.models import Rank
import forms

#TODO write function the takes code and returns amount. Transactional
class GiftCardRedeem(FormView):
    model = GiftCard
    form_class = GiftCardCheck
    template_name = 'settings/redeem.html'
    success_url = '/settings/finance/redeem/success/'

    def form_valid(self, form):
        try:
            singlegiftcard = GiftCard.objects.get(code=form.cleaned_data['giftcode'], used=False)
            singlegiftcard.used = True
            singlegiftcard.save()
            balance = self.request.user.userprofile.balance
            totalbal = balance + singlegiftcard.worth
            self.request.user.userprofile.balance = totalbal
            self.request.user.userprofile.save()
            return HttpResponseRedirect(self.get_success_url())
        except:
            return HttpResponseRedirect('/settings/finance/redeem/error/')


# Change the users rank
class FinancePage(FormView):
    model = Rank
    template_name = 'settings/finance.html'
    form_class = RankChanger
    success_url = '/settings/finance/upgrade/success/'

    def form_valid(self, form):
        GiftCardCheck = form.save(commit=False)
        balance = self.request.user.userprofile.balance
        rank = form.cleaned_data['rank']
        if balance >= rank.price:
            total = balance - rank.price
            self.request.user.userprofile.balance = total
            self.request.user.userprofile.rank = rank
            self.request.user.userprofile.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('/settings/finance/upgrade/error/')

