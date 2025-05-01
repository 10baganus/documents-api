from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from webapp.models import User, Document
from django.contrib.auth import authenticate

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    Кастомный сериализатор для JWT, использующий email вместо username
    '''
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        credentials = {
            'email': attrs.get("email"),
            'password': attrs.get("password")
        }

        user = authenticate(**credentials)

        if user is None or not user.is_active:
            raise serializers.ValidationError("Неверный email или пароль.")

        data = super().validate(attrs)
        data["user"] = {
            "id": user.id,
            "email": user.email
        }
        return data


class UserSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для отображения информации о пользователе
    '''
    class Meta:
        model = User
        fields = ["id", "email"]


class RegisterSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для регистрации нового пользователя
    '''
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    '''
    Сериализатор для авторизации (не используется с JWT, но может пригодиться)
    '''
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверный email или пароль")


class DocumentSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели Document
    '''
    owner = serializers.ReadOnlyField(source='owner.email')  # Только для чтения — email владельца

    class Meta:
        model = Document
        fields = ["id", "title", "description", "file", "owner", "created_at"]
