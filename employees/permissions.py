from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Not an owner.'

    def has_object_permission(selfself, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return TRUE
        return request.user == obj.owner