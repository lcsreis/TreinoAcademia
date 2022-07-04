from rest_framework.serializers import ModelSerializer
from alunos_treinos.models import AlunoTreino

class AlunoTreinoSerializer(ModelSerializer):
    class Meta:
        model = AlunoTreino
        fields = ['id', 'aluno', 'nome', 'exercicios']