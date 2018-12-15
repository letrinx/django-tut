from rest_framework import permissions


class UserTestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # import pdb; pdb.set_trace()
        if request.user.username == 'admin' and request.user.is_superuser:
            return True