from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Membre
from .forms import InscriptionForm
from django.contrib import messages
from django.contrib.auth.models import User


# Vue pour le tableau de bord de l'administrateur
@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# Vue pour le tablfueau de borddu formateur
@login_required
def formateur_dashboard(request):
    return render(request, 'formateur_dashboard.html')


# Vue pour le tableau de bord du membre
from django.contrib.auth.decorators import login_required

@login_required
def membre_dashboard(request):
    return render(request, 'membre_dashboard.html')


# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        password = request.POST['password']
        role = request.POST['role']

        # Vérification de l'utilisateur dans la table Membre
        try:
            membre = Membre.objects.get(nom=nom, prenom=prenom)
            if membre.check_password(password):  # Vérification du mot de passe haché
                if membre.role == role:  # Vérification du rôle
                    if role == "admin":
                        return redirect('admin_dashboard')
                    elif role == "formateur":
                        return redirect('formateur_dashboard')
                    elif role == "membre":
                        return redirect('membre_dashboard')
                else:
                    messages.error(request, "Le rôle sélectionné ne correspond pas à votre compte.")
                    return redirect('connexion')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
                return redirect('connexion')
        except Membre.DoesNotExist:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
            return redirect('connexion')

    return render(request, 'connexion.html')


# Vue pour l'inscription
def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            membre = form.save(commit=False)
            membre.set_password(form.cleaned_data['mot_de_passe'])  # Hacher le mot de passe
            membre.save()
            messages.success(request, "Inscription réussie")
            if membre.role == 'membre':
                return redirect('membre_dashboard')
            elif membre.role == 'admin':
                return redirect('admin_dashboard')
            elif membre.role == 'formateur':
                return redirect('formateur_dashboard')
        else:
            messages.error(request, form.errors)  # Affiche li erreurs de formulaire
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def bienvenue_view(request):
    return render(request, 'base.html')


from django.shortcuts import render

  # Vérifiez que le nom du template esti

def Accueil(request):
    return render(request, 'Accueil.html')


from django.core.paginator import Paginator
from .models import Produit,Commande


def marche_view(request):
    query = request.GET.get('q', '')  # Récupérer le terme de recherche
    produits = Produit.objects.all()

    if query:
        # Filtrer les produits en fonction de la recherche
        produits = produits.filter(titre__icontains=query)

    paginator = Paginator(produits, 8)  # 8 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query  # Passer le termrioe de recherche dans le contexte
    }
    return render(request, 'marché.html', context)


def gestion_membre(request):
    membres = Membre.objects.all()  # Récupère tous les membres
    return render(request, 'gestion_membre.html', {'membres': membres})


from django.shortcuts import render, get_object_or_404
from .models import Produit

def detail_view(request, produit_id):
    # Récupérer le produit en fonction de l'ii, ou renvoyer une erreur 404 s'il n'existe pas
    produit = get_object_or_404(Produit, id=produit_id)
    
    # Passer le produit dans le contexte pour l'utiliser dans le template
    return render(request, 'detail.html', {'produit': produit})


from django.shortcuts import render, redirect
from .models import Commande
import json
from django.shortcuts import render, redirect
from .models import Commande

def checkout(request):
    if request.method == 'POST':
        # Récupérer les données du panier
        items = request.POST.get('items', '[]')  # Valeur par défaut '[]' si rien n'est envoyé
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        code_postal = request.POST.get('code_postal')

        if items == '[]' or not items:
            return render(request, 'checkout.html', {'error': 'Le panier est vide ou invalide.'})

        # Conversion de la chaîne JSON en liste Python
        try:
            items_json = json.loads(items)
        except json.JSONDecodeError:
            return render(request, 'checkout.html', {'error': 'Données du panier invalides.'})

        # Enregistrer la commande dans la base de données
        commande = Commande(
            items=items_json,  # Stocker le panier en tant que JSON
            total=total,
            nom=nom,
            email=email,
            address=address,
            ville=ville,
            pays=pays,
            code_postal=code_postal,
        )
        commande.save()
        return redirect('paiement')

    return render(request, 'checkout.html')


def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    
    return render(request, 'confirmation.html', {'name':nom})


from django.shortcuts import render
from .models import Produit

def gestion_produit(request):
    produits = Produit.objects.all()
    return render(request, 'gestion_produit.html', {'produits': produits})



from django.shortcuts import render
from .models import Commande

def gestion_commandes(request):
    commandes = Commande.objects.all()  # Récupère toutes les commandes
    return render(request, 'gestion_commandes.html', {'commandes': commandes})


from django.shortcuts import render
from .models import Membre, Produit, Commande
from django.db.models import Count, Sum

def rapport(request):
    # Rapports sur les membres
    total_membres = Membre.objects.count()
    repartition_roles = Membre.objects.values('role').annotate(total=Count('role'))
    membres_actifs = Membre.objects.filter(role__in=['membre', 'formateur', 'admin']).count()  # Supposition des membres actifs

    # Rapports sur les produits
    meilleures_ventes = Produit.objects.all().order_by('-date_added')[:5]  # Top 5 des produits
    inventaire = Produit.objects.all()
    produits_en_rupture = Produit.objects.filter(prix=0)  # Produits qui ont un prix à 0 indiquant une rupture (à ajuster selon votre logique)

    # Rapports sur les commandes
    total_commandes = Commande.objects.count()
    valeur_commandes = Commande.objects.aggregate(total=Sum('total'))['total']
    taux_abandon_panier = 0  # Si vous suivez cela, vous pouvez ajouter une logique appropriée

    context = {
        'total_membres': total_membres,
        'repartition_roles': repartition_roles,
        'membres_actifs': membres_actifs,
        'meilleures_ventes': meilleures_ventes,
        'inventaire': inventaire,
        'produits_en_rupture': produits_en_rupture,
        'total_commandes': total_commandes,
        'valeur_commandes': valeur_commandes,
        'taux_abandon_panier': taux_abandon_panier,
    }
    
    return render(request, 'rapport.html', context)


from django.shortcuts import render
from .models import Membre, Produit, Commande

from django.shortcuts import render
from .models import Membre  # Assurez-vous que votre modèle Membre est correctement importé

def dashboard_view(request):
    total_membres = Membre.objects.count()  # Compte le nombre total de membres
    total_produits = Produit.objects.count()  # Compte le nombre total de produits
    total_commandes = Commande.objects.count()  # Compte le nombre total de commandes
    
    # Vous pouvez également récupérer d'autres informations, comme les membres actifs, etc.
    context = {
        'total_membres': total_membres,
        'total_produits': total_produits,
        'total_commandes': total_commandes,
    }
    
    return render(request, 'admin_dashboard.html', context)



from django.shortcuts import render
from .models import FormationVideo, Quiz

def formations_view(request):
    videos = FormationVideo.objects.all()
    quizzes = Quiz.objects.all()
    return render(request, 'formations.html', {'videos': videos, 'quizzes': quizzes})



from django.shortcuts import render, redirect
from .models import Quiz

def quiz_submit(request):
    if request.method == 'POST':
        score = 0
        total_questions = Quiz.objects.count()

        for quiz in Quiz.objects.all():
            # Obtenir la réponse soumise par l'utilisateur pour chaque question
            user_answer = request.POST.get(f'quiz_{quiz.id}')
            
            # Vérifier si la réponse est correcte
            if user_answer == quiz.bonne_reponse:
                score += 1

        # Calculer le score et rediriger vers une page de résultats
        context = {
            'score': score,
            'total_questions': total_questions
        }
        return render(request, 'quiz_result.html', context)
    return redirect('formations')  # Si pas de POST, rediriger vers la page de formations


# views.py
from django.shortcuts import render
from .models import FormationVideo, Quiz

def videos_list(request):
    videos = FormationVideo.objects.all()  # Récupère toutes les vidéos
    return render(request, 'videos_list.html', {'videos': videos})

def quiz_page(request):
    quizzes = Quiz.objects.all()  # Récupère tous les quiz
    return render(request, 'quiz_page.html', {'quizzes': quizzes})


from django.shortcuts import render
from .models import Quiz

def gestion_quiz(request):
    quiz_list = Quiz.objects.all()  # Récupérer tous les quiz
    return render(request, 'gestion_quiz.html', {'quiz_list': quiz_list})

from .models import FormationVideo


def gestion_videos(request):
    video_list = FormationVideo.objects.all()  # Récupérer toutes les vidéos
    return render(request, 'gestion_videos.html', {'video_list': video_list})


from .models import Membre, Production

from django.shortcuts import render

def suivi_production(request):
    membres = Membre.objects.prefetch_related('productions').all()

    # Préparer une liste avec les membres et un indicateur de production
    membres_avec_productions = []
    for membre in membres:
        has_productions = membre.productions.exists()  # Vérification dans la vue
        membres_avec_productions.append({
            'membre': membre,
            'has_productions': has_productions,
            'productions': membre.productions.all() if has_productions else []
        })

    context = {
        'membres_avec_productions': membres_avec_productions
    }
    return render(request, 'suivi_production.html', context)

# Vue pour gérer la page de paiement


def paiement(request):
    return render(request, 'paiement.html')




