from django.contrib import admin
from .models import GiftCard


class GiftCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(GiftCard, GiftCardAdmin)
