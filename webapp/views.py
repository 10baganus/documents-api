from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from webapp.permissions import IsOwnerOrReadOnly
from webapp.models import Document
from webapp.serializers import CustomTokenObtainPairSerializer, RegisterSerializer, DocumentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    '''
    Контроллер для регистрации пользователя
    '''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    '''
    ViewSet для управления объектами Document
    '''
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomTokenObtainPairView(TokenObtainPairView):
    '''
    Кастомизированный класс получения JWT токена
    '''
    serializer_class = CustomTokenObtainPairSerializer
