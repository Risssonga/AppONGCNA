from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import user_Membre, profile


# <----| Enregistrement du model Profile dans la BD |---->
class profil_addUser(admin.StackedInline):
    model = profile

class profile_User(UserAdmin):
  inlines = (profil_addUser, )

admin.site.unregister(User)
admin.site.register(User, profile_User)



# <----| Enregistrement du model User_Membre dans la BD |---->
@admin.register(user_Membre)
class add_user(admin.ModelAdmin):
    list_display = ("id", "photo_profile", "Nom", "prenom", "Email", "Tel", "Role", "description")


