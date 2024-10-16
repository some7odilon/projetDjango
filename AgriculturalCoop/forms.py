from django import forms
from .models import Membre
from django.contrib.auth.hashers import make_password

class InscriptionForm(forms.ModelForm):
    password_repeat = forms.CharField(widget=forms.PasswordInput(), label="Confirmez le mot de passe")

    class Meta:
        model = Membre
        fields = ['nom', 'prenom', 'age', 'type_culture', 'email', 'mot_de_passe', 'role']
        widgets = {
            'mot_de_passe': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        mot_de_passe = cleaned_data.get("mot_de_passe")
        password_repeat = cleaned_data.get("password_repeat")

        if mot_de_passe != password_repeat:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data

    def save(self, commit=True):
        membre = super().save(commit=False)
        # Hacher le mot de passe avant de sauvegarder
        membre.mot_de_passe = make_password(self.cleaned_data["mot_de_passe"])
        if commit:
            membre.save()
        return membre
