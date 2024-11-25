from rest_framework import permissions


#python manage.py changepassword username


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions. SAFE_METHODS:
            return True
        return bool(request.user.is_staff and request.user)