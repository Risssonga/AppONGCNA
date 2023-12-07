import os

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout, login, admin
from django.contrib import messages
from .forms import MemberRegistration, UserRegistration, UserRegisterForm, ModifuserinfoRegistration
from .models import user_Membre
from .decorators import group_required

#---> NB: les lignes en surbrillances(Rouge) sont les Décorateurs (groups & permissions )


# <----| Fonction pour Authentifier  un User |---->

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.warning(request, "Identifiant ou mot de passe incorect !")
    fm = UserRegistration()
    return render(request, 'GestionApp/login.html', {'fm': fm})


# <----| Fonction pour Deconnecter un User |---->
def logout_user(request):
    logout(request)
    return redirect(login_user)


# <----| Fonction pour Ajouter un User |---->
@group_required(['super_Administrateur', 'Administrateur'])
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "utilisateur ajouter avec success !")
            return redirect(register_user)
    else:
        form = UserRegisterForm()
    return render(request, 'GestionApp/adduser.html', {'form': form})


# <----| Fonction pour Modifier un User |---->


@group_required(['super_Administrateur', 'Administrateur'])
def Modif_user_action(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = UserRegisterForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect(Gestion_user)
    else:
        form = UserRegisterForm()
    return render(request, 'GestionApp/modifuser.html', {'form': form})


# <----| Fonction pour suprimer un User |---->

def delete_User(request, id):
    if request.method == 'POST':
        poo = User.objects.get(id=id)
        poo.delete()
        messages.warning(request, "Utilisateur supprimer !")
        return redirect(view_User)


# <----| Définition de la vue page Index(Home) |---->
def index(request):
    labels = []
    data = []
    queryset = user_Membre.objects.all()
    for person in queryset:
        labels.append(person.Nom)
        data.append(person.id)
    rec = User.objects.all()
    alli = len(rec)
#print(alli)
    recup_listes = user_Membre.objects.all()
    mbr_all = len(recup_listes)
#print(mbr_all)
    return render(request, 'GestionApp/index.html',
                  {'rl': rec,
                          'all': alli, 'mbr_all': mbr_all,
                          'll': recup_listes,
                          'labels': labels,
                           'data': data
                   })


# <----| Fonction pour Ajouter un Membre |---->
@group_required(['super_Administrateur', 'Manager'])
def add_membre(request):
    if request.method == 'POST':
        formulaire = MemberRegistration(request.POST, request.FILES)
        if formulaire.is_valid():
            pp = formulaire.cleaned_data['photo_profile']
            nm = formulaire.cleaned_data['Nom']
            pn = formulaire.cleaned_data['prenom']
            em = formulaire.cleaned_data['Email']
            tl = formulaire.cleaned_data['Tel']
            rl = formulaire.cleaned_data['Role']
            dp = formulaire.cleaned_data['description']
            reg = user_Membre(photo_profile = pp, Nom = nm, prenom = pn, Email = em, Tel = tl, Role = rl, description = dp )
            reg.save()
            messages.info(request, "Membre ajouter avec success !")
            return redirect(add_membre)
    else:
        formulaire = MemberRegistration()
    return render(request, 'GestionApp/form1.html', {'form': formulaire})


# <----| Fonction pour suprimer un Membre |---->
@group_required('super_Administrateur')
def delete_membre(request, id):
    if request.method == 'POST':
        pi = user_Membre.objects.get(id=id)
        pi.delete()
        messages.warning(request, "Membre suprimer !")
        return redirect(suprimuser)
#        return redirect(index)

# <----|Définition de la vue page Suprimer un membre  |---->
@group_required(['super_Administrateur', 'Administrateur'])
def suprimuser(request):
#       if request.user.groups.filter(name='super_Administrateur').exists():
        membres = user_Membre.objects.all()
        return render(request, 'GestionApp/suprimMembre.html',  {'membres': membres})
#    else:
#        return redirect(erreur404)


# <----| Fonction pour modifier les infos d'un Membre |---->
@group_required(['super_Administrateur', 'Manager', 'Administrateur'])
def modiform(request):

    membres = user_Membre.objects.all()
    return render(request, 'GestionApp/modiform.html', {'membres': membres})


# <----| Fonction pour Enregistrer les infos Modifier |---->

def edit(request, id):
    membre = user_Membre.objects.get(id=id)
    return render(request, 'GestionApp/modiform2.html',{'membre':membre})

def Update(request, id):
    membre = user_Membre.objects.get(id=id)
    fom = MemberRegistration(request.POST,request.FILES, instance=membre)
    if fom.is_valid():
        fom.save()
        messages.success(request, "Modification effectuer avec success !")
        return redirect(modiform)

    return render(request, 'GestionApp/modiform2.html',{'membre':membre})




# <----| Définition de la vue page Voir les User |---->
def view_User(request):
    recup_liste = User.objects.all()
    rec = len(recup_liste)
    return render(request, 'GestionApp/viewUser.html', {'rl': recup_liste, 'all': rec })


# <----| Définition de la vue page Profil |---->
def profil(request):
   # membre = User.objects.get()
    return render(request, 'GestionApp/profile.html')

# <----| Définition de la page Table des Membre |---->
def table_membre(request):
    recup_liste = user_Membre.objects.all()
    mbr_all = len(recup_liste)
    return render(request, 'GestionApp/tablemebre.html', {'rl': recup_liste, 'mbr_all':mbr_all })


# <----|Définition de la vue page Gestion des utilisateur  |---->
@group_required(['super_Administrateur', 'Administrateur'])
def Gestion_user(request):
#       if request.user.groups.filter(name='super_Administrateur').exists():
        recup_liste = User.objects.all()
        return render(request, 'GestionApp/gestionUser.html',  {'rl': recup_liste})
#    else:
#        return redirect(erreur404)


# <----| Définition de la vue page Erreur 404 |---->
def erreur404(request):
    return render(request, 'GestionApp/404.html')


# <----| Définition de la vue page Calendrier |---->
def calendier(request):
    return render(request, 'GestionApp/calendar.html')



#<----| Définition de la vue page Calendrier |---->


def todolist(request):
    return render(request, 'GestionApp/todoliste.html')





# <----| Définition de la vue page Index(Home) |---->
def base(request):
    return render(request, 'GestionApp/base.html')


