from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from webapp.views import CustomTokenObtainPairView, RegisterView, DocumentViewSet

# Создание маршрутизатора DRF и регистрация ViewSet для модели Document
router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
