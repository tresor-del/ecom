from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, RegisterSerializer
from .models import CustomUser
from .permissions import IsReadOnlyOrAdmin
from .mixins import CreateUserMixin



# Voir les détails d'un utilisateur , Mettre a jour ou supprimer un utilisateur si on est administrateur
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsReadOnlyOrAdmin]

# Liste tous les utilisateurs ou creer un nouveau si on est administrateur
class UserListView(CreateUserMixin, generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =RegisterSerializer
    permission_classes = [IsReadOnlyOrAdmin]
      

class RegisterView(CreateUserMixin, generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


