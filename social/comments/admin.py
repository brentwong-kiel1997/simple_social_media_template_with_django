from django.contrib import admin
from .models import Post_comment, Event_comment
# Register your models here.

admin.site.register(Post_comment)
admin.site.register(Event_comment)