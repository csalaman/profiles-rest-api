from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
          
    #  Check if authenticated user has permission
    def has_object_permission(self, request, view, obj):
        """Check if user is attempting to edit their own profile"""

        # Check methods are read-only types, allow users to see other users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, check if object belongs to requesting user
        return obj.id == request.user.id