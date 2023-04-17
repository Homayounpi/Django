from django.contrib import admin
from .models import Relation,Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Relation)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
class ExtendeUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User,ExtendeUserAdmin)






