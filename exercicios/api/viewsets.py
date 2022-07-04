from rest_framework.viewsets import ModelViewSet
from exercicios.api.serializers import ExercicioSerializer
from exercicios.models import Exercicio

class ExercicioViewSet(ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer