from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user