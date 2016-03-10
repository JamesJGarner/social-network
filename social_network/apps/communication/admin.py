from django.contrib import admin
from .models import Message, Reply


class ReplyAdmin(admin.TabularInline):
    extra = 1
    model = Reply


class MessageAdmin(admin.ModelAdmin):
    inlines = [ReplyAdmin]

admin.site.register(Message, MessageAdmin)


