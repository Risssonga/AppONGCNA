from django import forms
from django.contrib.auth.models import User
from .models import user_Membre, profile
from django.contrib.auth.forms import UserCreationForm


# <----| Définition du formulaire d'enregistrement d'un User |---->
class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name':  'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'nom',
            'maxlength': '16',
            'minilength': '4'
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email@gmail.com'
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Mot de passe',
            'maxlength': '22',
            'minilength': '8'
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'comfirme Mot de passe',
            'maxlength': '22',
            'minilength': '8'
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# <----| Définition du formulaire d'enregistrement d'un Membre |---->
class MemberRegistration(forms.ModelForm):
    class Meta:
        model = user_Membre
        fields = ['photo_profile','Nom', 'prenom', 'Email', 'Tel', 'Role', 'description']
        widgets = {
            'photo_profile': forms.FileInput(attrs={'class': 'form-control'}),
            'Nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'prenom'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email@gmail.com'}),
            'Tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de téléphone'}),
            'Role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ajouter une description'})

        }


# <----| Définition du formulaire de connexion (login) |---->
class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Nom d'utilisateur"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),

        }

class ModifuserinfoRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Nom d'utilisateur"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Nom"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': "Prenom"}),

        }
