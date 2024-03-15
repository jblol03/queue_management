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
        return f"{self.sub_category, self.category}"
   
class Organization (models.Model):
    organization = models.CharField(max_length = 300, unique = True)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)    
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.organization