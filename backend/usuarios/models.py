from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

class Funcionario(Usuario):
    super().__init__()
    cargo = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)

class Paciente(Usuario):
    super().__init__()
    data_nascimento = models.DateField()
    diagnostico = models.CharField(max_length=80)
    nome_responsavel = models.CharField(max_length=100)
    telefone_responsavel = models.CharField(max_length=15)
    info_adicionais = models.TextField()