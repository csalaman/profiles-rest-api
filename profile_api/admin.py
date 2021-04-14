from django.contrib import admin
from profile_api import models
 
#  Registers model for django admin
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)