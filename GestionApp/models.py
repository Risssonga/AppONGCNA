from django.db import models
from django.contrib.auth.models import User



# <----| Définition du model Pofile qui servira de container a image |---->



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='user0.png', upload_to='images')

#    def __str__(self):
#        return f'{self.user.username}profile'





# <----| Définition du model type user_menbre de l'ONG |---->
class user_Membre(models.Model):
    photo_profile = models.ImageField(null='Tue', blank=True, upload_to='images', default='user0.png')
    Nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    Tel = models.CharField(max_length=10)
    Role = models.CharField(max_length=45)
    description = models.TextField(max_length=150)


# <----| Définition du model Utilisateur qui servira de container a image |---->



class Utlilisateur(models.Model):
    nom = models.CharField(max_length=35)
    prenom = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    picture = models.ImageField(null='Tue', blank=True, upload_to='images')













