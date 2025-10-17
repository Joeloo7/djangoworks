from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    pages=models.IntegerField()
    language=models.CharField(max_length=100)
    image=models.ImageField(upload_to="books")
# Create your models here.
