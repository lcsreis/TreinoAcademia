from django.db import models

class Aluno(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=300)
    idade = models.IntegerField()
    datacriado = models.DateTimeField(auto_now_add=True)
    dataatualizado = models.DateTimeField(null=True)

    def __str__(self):
        return self.cpf
