from rest_framework.permissions import BasePermission


class IsTransactionOwner(BasePermission):
    """
    Разрешение, проверяющее, что пользователь является владельцем транзакции.
    """
    def has_object_permission(self, request, view, obj):
        # Проверяем, что пользователь обновляет только свои собственные транзакции
        return obj.user == request.user


class IsAdminUser(BasePermission):
    """
    Разрешение, проверяющее, что пользователь является администратором.
    """
    def has_permission(self, request, view):
        # Проверяем, что пользователь является администратором
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(BasePermission):
    """
    Пользовательские разрешения для проверки владельца объекта.
    Разрешает только владельцу объекта выполнять редактирование.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешение только для чтения для всех запросов GET, HEAD или OPTIONS.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Проверяем, является ли пользователь владельцем объекта.
        return obj.user == request.user


class IsExchangePairOwner(BasePermission):
    """
    Разрешение, проверяющее, что пользователь является владельцем пары обмена.
    """
    def has_object_permission(self, request, view, obj):
        # Проверяем, является ли пользователь владельцем пары обмена.
        return obj.base_currency.user == request.user



# from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
# from .models import Transaction

# def create_custom_permissions():
#     content_type = ContentType.objects.get_for_model(Transaction)
#     permission, created = Permission.objects.get_or_create(
#         codename='view_transaction',
#         name='Can view transactions',
#         content_type=content_type,
#     )
#     return permission

