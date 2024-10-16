
from django.contrib import admin
from .models import Membre, Produit, Commande, FormationVideo, Quiz,Production

class AdminMembre(admin.ModelAdmin):
    list_display = ('nom' , 'prenom' , 'type_culture', 'role', 'date_added')
    list_filter = ('role',) 



class AdminProduit(admin.ModelAdmin):
    list_display = ('titre', 'prix', 'date_added')
    search_fields = ('titre',)
    list_editable = ('prix',)


class AdminCommande(admin.ModelAdmin):
    list_display = ('items' ,'nom' , 'email', 'address', 'ville', 'total', 'date_commande')



class AdminFormationVideo(admin.ModelAdmin):
    list_display = ('titre' , 'url_video' , 'date_publication')


class AdminQuiz(admin.ModelAdmin) :
    list_display = ('question' , 'choix_1' , 'choix_2' , 'choix_3' , 'bonne_reponse' )


class AdminProduction(admin.ModelAdmin):
    list_display = ('membre' , 'date_debut' , 'date_fin', 'quantite_produite' , 'superficie')


admin.site.register(Membre, AdminMembre)
admin.site.register(Produit, AdminProduit)
admin.site.register(Commande, AdminCommande)
admin.site.register(FormationVideo, AdminFormationVideo)
admin.site.register(Quiz , AdminQuiz)
admin.site.register(Production , AdminProduction)

