from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            # Get access to superuser
            request.user.is_authenticated and
            request.user.is_superuser or
            # Get access to author of the object
            obj.author == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            # Get access to Authors read only
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_staff or
            # Get full access to Superuser
            request.user and request.user.is_superuser
        )



