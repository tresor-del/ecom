from django.db import models
from authentication.models import CustomUser
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=100)

    slug = models.SlugField(unique=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    price = models.FloatField(default=0.00) # prix actuel
    original_price = models.FloatField(null=True, blank=True) # prix de base
    discount_percentage = models.FloatField(default=0.0) # pourcentage de reduction

    stock_quantity = models.PositiveIntegerField(default=0)
    sold_count = models.PositiveIntegerField(default=0)

    description = models.TextField(max_length=500)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/products/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    average_rating = models.FloatField(default=0.0) # moyenne des evaluations
    rating_count = models.PositiveIntegerField(default=0) # nombre d'
    

    def __str__(self):
        return self.title

    def has_discount(self):
        """
        methode pour vérifier si un produit est en promotion

        """
        return self.discount_percentage > 0 and self.original_price is not None
    

    def calculate_price(self):
        """
        calcule du prix final en fonction du pourcentage de réduction et du prix de base

        """
        if self.original_price and self.discount_percentage > 0:
            self.price = self.original_price * (1 - self.discount_percentage / 100)
        return self.price
    
    def add_rating(self, new_rating):
        """
        Ajoute une nouvelle évaluation et met à jour la moyenne.
        :param new_rating: La nouvelle note donnée par un utilisateur (1 à 5).
        """
        total_score = self.average_rating * self.rating_count  # Calcul du score total actuel
        self.rating_count += 1  # Incrémenter le nombre d'évaluations
        total_score += new_rating  # Ajouter la nouvelle note
        self.average_rating = total_score / self.rating_count  # Recalculer la moyenne
        self.save()  # Sauvegarder les changements

    def remove_rating(self, removed_rating):
        """
        Supprime une note et met à jour la moyenne.
        :param removed_rating: La note qui est supprimée.
        """
        if self.rating_count > 1:
            total_score = self.average_rating * self.rating_count
            total_score -= removed_rating  # Soustraire la note supprimée
            self.rating_count -= 1
            self.average_rating = total_score / self.rating_count
        else:
            # Si c'était la dernière évaluation, réinitialiser
            self.reset_ratings()
        self.save()


    
    def reset_ratings(self):
        """
        Réinitialise la moyenne des évaluations et le compteur.
        """
        self.average_rating = 0.0
        self.rating_count = 0
        self.save()

    def update_ratings(self):
        """
        Recalcule la moyenne et le nombre d'évaluations à partir du modèle lié.
        """
        ratings = self.ratings.all()
        self.rating_count = ratings.count()
        self.average_rating = ratings.aggregate(models.Avg('rating'))['rating__avg'] or 0.0
        self.save()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        self.calculate_price()

        super().save(*args, **kwargs)


class ProductRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Utilisateur ayant laissé l’évaluation
    rating = models.PositiveIntegerField()  # Note entre 1 et 5
    comment = models.TextField(blank=True, null=True)  # Commentaire facultatif
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.title} : {self.rating}"


    