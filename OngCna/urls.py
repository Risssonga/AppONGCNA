from django.contrib import admin
from django.urls import path
from GestionApp import views
from django.conf import settings
from django.conf.urls.static import static


# <----| Liste des url parents de l'app |---->
urlpatterns = [

    path('admin/', admin.site.urls),
    path('index/', views.index, name="Home"),

    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    path('formulaire/', views.add_membre, name="form"),
    path('delete/<int:id>/', views.delete_membre, name="deletemembre"),
    path('deleteUser/<int:id>/', views.delete_User, name="deleteUser"),
#    path('modif membres/<int:id>/', views.update_member, name="updatemember"),
    path('modiform/', views.modiform, name="modiform"),
    path('gestion des utilisateur/', views.Gestion_user, name="Gestuser"),
    path('calendrier/', views.calendier, name="calendrier"),
    path('liste des tache/', views.todolist, name="todo"),
    path('<int:id>/', views.Modif_user_action, name="modifuser"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.Update, name="update"),
    path('update/<int:id>/', views.Update, name="cccccc"),
    path('add user/', views.add_membre, name="adduser"),


    path('viewUser/', views.view_User, name="viewUser"),
    path('profile/', views.profil, name="profil"),
    path('SuprimUser/', views.suprimuser, name="suprimbr"),
 #   path('modifmenber/', views.modif_member, name="modifmembre"),
    path('table de menber/', views.table_membre, name="table"),
    path('Errore page/', views.erreur404, name="Errore"),
    path('base/', views.base, name="base"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
