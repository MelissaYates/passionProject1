from django.contrib import admin
from .models import Message, UserProfile
# from .models import Users, Chat

# Register your models here.
admin.site.register(Message)
admin.site.register(UserProfile)

# admin.site.register(Users)
# admin.site.register(Chat)