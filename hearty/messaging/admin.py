from django.contrib import admin
from .models import Message


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['chat', 'sender', 'created_at']
    list_filter = ['chat', 'created_at', 'sender']
    list_editable = ['sender']
    using = 'mongodb'

    def get_queryset(self, request):

        return super().get_queryset(request).using('mongodb')