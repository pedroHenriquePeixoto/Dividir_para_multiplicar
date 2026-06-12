from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ("Pending", "Pendente"),
    ("Aproved", "Aprovado"),
    ("Rejected", "Rejeitado"),
)

class Course(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    category = models.ForeignKey('Category', on_delete=models.PROTECT,null=True, blank=True)
    
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name