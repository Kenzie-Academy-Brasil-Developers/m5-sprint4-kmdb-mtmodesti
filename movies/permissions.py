from urllib import request
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return "modesti" in request.user.email