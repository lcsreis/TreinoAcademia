from rest_framework.viewsets import ModelViewSet
from alunos_treinos_exercicios.api.serializers import AlunoTreinoExercicioSerializer
from alunos_treinos_exercicios.models import AlunoTreinoExercicio


class AlunoTreinoExercicioViewSet(ModelViewSet):
    queryset = AlunoTreinoExercicio.objects.all()
    serializer_class = AlunoTreinoExercicioSerializer