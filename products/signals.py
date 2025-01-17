from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductRating, Product
from django.db.models import Avg, Count

@receiver(post_save, sender=ProductRating)
def update_product_ratings(sender, instance, created, **kwargs):
    if created:
        product = instance.product  # L'évaluation est liée au produit
        product.rating_count = product.ratings.count()  # Met à jour le nombre d'évaluations
        product.average_rating = product.ratings.aggregate(Avg('rating'))['rating__avg']  # Met à jour la moyenne des évaluations
        product.save()
