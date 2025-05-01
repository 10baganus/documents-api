from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Кастомное разрешение: только владелец объекта может изменять его,
    остальные пользователи могут только просматривать (read-only).
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
