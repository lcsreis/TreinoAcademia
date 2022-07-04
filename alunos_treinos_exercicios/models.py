from django.db import models
from alunos_treinos.models import AlunoTreino
from exercicios.models import Exercicio

class AlunoTreinoExercicio(models.Model):
    treino = models.ForeignKey(AlunoTreino)
    exercicio = models.ForeignKey(Exercicio)
    repeticoes = models.IntegerField()
    peso = models.IntegerField()
    #tipopeso - models.CharField()
