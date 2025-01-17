from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateProductView.as_view(), name='list-create-product'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('rating/', views.ProductRatingCreateView.as_view(), name='rating')
]
