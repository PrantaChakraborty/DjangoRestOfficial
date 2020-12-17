from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    # custom permission
    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permission are only allowed to the owner of the snippet
        return obj.owner == request.user
