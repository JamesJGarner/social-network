from django.contrib import admin
from .models import Post, Reply


class ReplyAdmin(admin.TabularInline):
    extra = 1
    model = Reply


class PostAdmin(admin.ModelAdmin):
	inlines = [ReplyAdmin]

admin.site.register(Post, PostAdmin)

