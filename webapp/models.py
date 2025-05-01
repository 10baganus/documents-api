from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from webapp.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    '''
    Кастомная модель пользователя с авторизацией по email
    '''
    email = models.EmailField("Email", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Document(models.Model):
    '''
    Модель документа, загружаемого пользователем
    '''
    file = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_docs'
        ordering = ['created_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
