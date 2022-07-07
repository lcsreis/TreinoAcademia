from django.db import models
from django.utils import timezone
from alunos.models import Aluno
from exercicios.models import Exercicio

class AlunoTreino(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=300)
    ativo = models.BooleanField(default=True)
    datacriado = models.DateTimeField(auto_now_add=True)
    dataatualizado = models.DateTimeField(null=True)

    def __str__(self):
        return self.nome
