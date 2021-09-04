from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from feedthepuss.models import Pet, User


admin.site.register(User, UserAdmin)
admin.site.register(Pet)
