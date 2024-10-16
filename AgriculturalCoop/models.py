from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    type_culture = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('formateur', 'Formateur'),
        ('membre', 'Membre'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='membre')

    def set_password(self, raw_password):
        self.mot_de_passe = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.mot_de_passe)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Produit(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()  # 'description' en minuscule
    image = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.titre


from django.db import models

class Commande(models.Model):
    items = models.JSONField() 
    total = models.DecimalField(max_digits=10, decimal_places=2)
    nom = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=200)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']


    def __str__(self):
        return self.nom


class FormationVideo(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    url_video = models.URLField()  # Lien vers la vidéo
    date_publication = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre

class Quiz(models.Model):
    question = models.CharField(max_length=255)
    choix_1 = models.CharField(max_length=255)
    choix_2 = models.CharField(max_length=255)
    choix_3 = models.CharField(max_length=255)
    bonne_reponse = models.CharField(max_length=255)


    def __str__(self):
        return self.question



class Production(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='productions')
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    quantite_produite = models.DecimalField(max_digits=10, decimal_places=2)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    commentaire = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Production de {self.membre.nom} ({self.superficie})"