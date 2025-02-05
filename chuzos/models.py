from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class ChuzoReview(models.Model):
    name = models.TextField()
    price = models.PositiveIntegerField()
    price_quantity_ratio = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    cheese_review = models.TextField(null=True)
    cheese_quantity = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    protein_review = models.TextField(null=True)
    potato_review = models.TextField(null=True) 
    tartar_review = models.TextField(null=True)
    pineapple_review = models.TextField(null=True)
    grille_review = models.TextField(null=True)
    special_sauce_review = models.TextField(null=True)
    bollo_review = models.TextField(null=True)
    photo_url = models.TextField(null=True)
    visited_at = models.DateTimeField()
    additional_comments = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name