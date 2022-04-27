from unicodedata import name
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group

from api.serializers import UserSerializer
from queijaria.models import User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Exibindo todos os alunos e alunas"""

    
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(username=user)
        return queryset

