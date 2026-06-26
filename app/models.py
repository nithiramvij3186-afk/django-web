from django.db import models
# Create your models here.
class menu(models.Model):
    menu_name=models.CharField(max_length=100)
    menu_price=models.IntegerField()
    menu_description=models.TextField()
    menu_image=models.ImageField()

    def __str__(self):
        return self.menu_name

