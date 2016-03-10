from django.contrib import admin
from .models import UserProfile, Rank


class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)


class RankAdmin(admin.ModelAdmin):
    pass

admin.site.register(Rank, RankAdmin)

