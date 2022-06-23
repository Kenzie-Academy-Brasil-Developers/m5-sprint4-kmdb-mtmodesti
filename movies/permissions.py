from urllib import request
from rest_framework import permissions

class IsOWner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('entrei no isOwner')
        print('-----------'*50)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user