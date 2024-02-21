from django.db import models

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length = 300, unique = True)

    def __str__(self):
        return self.category

class Sub_Category (models.Model):
    sub_category = models.CharField(max_length = 300, unique = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category
    def __str__(self):
        return self.category

