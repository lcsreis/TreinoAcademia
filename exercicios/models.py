from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    datacriado = models.DateTimeField(auto_now_add=True)
    dataatualizado = models.DateTimeField(null=True)

    def __str__(self):
        return self.nome
