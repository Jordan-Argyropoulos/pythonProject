from django.contrib import admin
from . models import Infirmieres, Soins, Rapport, Prescription, \
    Passages, Tournees, NumeroTournee, Mutuelles, Medecin, Kine, Fiche, Patient, Equipe, Anamnese, Adresse

# Register your models here.

admin.site.register(Infirmieres)
admin.site.register(Soins)
admin.site.register(Adresse)
admin.site.register(Prescription)
admin.site.register(Rapport)
admin.site.register(Passages)
admin.site.register(Tournees)
admin.site.register(NumeroTournee)
admin.site.register(Mutuelles)
admin.site.register(Medecin)
admin.site.register(Kine)
admin.site.register(Fiche)
admin.site.register(Patient)
admin.site.register(Equipe)
admin.site.register(Anamnese)