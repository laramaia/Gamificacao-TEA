from django.db import models

class Clinica(models.Model):
    id_clinica = models.IntegerField()
    nome_clinica = models.CharField(max_length=50)