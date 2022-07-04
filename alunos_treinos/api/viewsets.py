from rest_framework.viewsets import ModelViewSet
from alunos_treinos.api.serializers import AlunoTreinoSerializer
from alunos_treinos.models import AlunoTreino

class AlunoTreinoViewSet(ModelViewSet):
    queryset = AlunoTreino.objects.all()
    serializer_class = AlunoTreinoSerializer