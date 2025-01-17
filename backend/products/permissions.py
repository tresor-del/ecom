from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    La permission pour permettre à un utilisateur de modifier ou supprimer un produit
    seulement si l'utilisateur est le propriétaire du produit.
    """

    def has_object_permission(self, request, view, obj):
        # Permet l'accès en lecture (GET, HEAD, OPTIONS) à tout le monde
        if request.method in permissions.SAFE_METHODS:
            return True

        # Vérifie que l'utilisateur est le propriétaire du produit
        return obj.owner == request.user
