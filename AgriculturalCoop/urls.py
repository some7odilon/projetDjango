from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.bienvenue_view, name='bienvenue'),  # Redirige l'URL racine vers la page de connexion
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('formateur-dashboard/', views.formateur_dashboard, name='formateur_dashboard'),
    path('membre-dashboard/', views.membre_dashboard, name='membre_dashboard'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('connexion/', views.login_view, name='connexion'), 
    path('Accueil/', views.Accueil, name='Accueil'),
    path('marche/', views.marche_view, name='marché'),
    path('gestion_membre/', views.gestion_membre, name='gestion_membre'),
    path('produit/<int:produit_id>/', views.detail_view, name='detail'),
    path('checkout', views.checkout,name="checkout"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('confirmation', views.confirmation, name='confirmation' ),
    path('gestion-produit/', views.gestion_produit, name='gestion_produit'),
    path('commandes/', views.gestion_commandes, name='gestion_commandes'),
    path('rapport/', views.rapport, name='rapport'),
    path('formations/', views.formations_view, name='formations'),
    path('quiz/submit/', views.quiz_submit, name='quiz_submit'),
    path('videos/', views.videos_list, name='videos_list'),  # Page dtes vidéos
    path('quiz/', views.quiz_page, name='quiz_page'),  # Page des quiz
    path('gestion-quiz/', views.gestion_quiz, name='gestion_quiz'),
    path('gestion-videos/', views.gestion_videos, name='gestion_videos'),
    path('suivi_production/', views.suivi_production, name='suivi_production'),
    path('paiement/', views.paiement, name='paiement'),

    
]
