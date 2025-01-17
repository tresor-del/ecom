from rest_framework import generics, permissions

from . import serializers
from . import models
from .permissions import IsOwnerOrReadOnly

class CreateProductView(generics.ListCreateAPIView):
    serializer_class = serializers.CreateProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

class ProductRatingCreateView(generics.CreateAPIView):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all()
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)