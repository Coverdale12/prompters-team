from django.contrib import admin

from .models import *

admin.site.register(PrivateMessage)
admin.site.register(Topic)
admin.site.register(TopicMessage)
admin.site.register(File)
admin.site.register(PrivateMessageHasFile)
admin.site.register(TopicMessageHasFile)
admin.site.register(Notification)
