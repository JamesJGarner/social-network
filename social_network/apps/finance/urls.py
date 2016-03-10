from django.conf.urls import patterns, include, url
from .views import GiftCardRedeem, FinancePage

urlpatterns = [
	url(r'^settings/finance/redeem/$', GiftCardRedeem.as_view(), name="redeem_page"),
    url(r'^settings/finance/upgrade/$', FinancePage.as_view(), name="Finance_Page"),
]
