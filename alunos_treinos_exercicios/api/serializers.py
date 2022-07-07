from rest_framework.serializers import ModelSerializer
from alunos_treinos_exercicios.models import AlunoTreinoExercicio

class AlunoTreinoExercicioSerializer(ModelSerializer):
    class Meta:
        model = AlunoTreinoExercicio
        fields = ['id', 'treino', 'exercicio', 'repeticoes', 'peso', 'tipopeso']
