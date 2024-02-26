from django.db import models

# Create your models here.
class Phone(models.Model):

    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f'''{self.id}, {self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'''
