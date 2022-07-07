from django.db import models
from alunos_treinos.models import AlunoTreino
from exercicios.models import Exercicio

class AlunoTreinoExercicio(models.Model):
    TIPOPESO_CHOICES = (
        ("UN", "Unidade"),
        ("TOT", "Total"),
        ("NA", "Não se aplica")
    )

    treino = models.ForeignKey(AlunoTreino, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    repeticoes = models.IntegerField()
    peso = models.IntegerField()
    tipopeso = models.CharField(max_length=200, choices=TIPOPESO_CHOICES, blank=False, null=False, default="NA")
    datacriado = models.DateTimeField(auto_now_add=True)
    dataatualizado = models.DateTimeField(null=True)

    def __str__(self):
        return self.treino