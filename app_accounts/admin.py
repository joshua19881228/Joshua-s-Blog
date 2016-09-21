from django.contrib import admin
from models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_user', 'profile_level')


admin.site.register(Profile, ProfileAdmin)