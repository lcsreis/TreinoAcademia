from rest_framework.viewsets import ModelViewSet
from alunos.api.serializers import AlunoSerializer
from alunos.models import Aluno

class AlunoViewSet(ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer