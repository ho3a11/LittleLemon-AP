from django.db import models



class Booking(models.Model):

    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    guest_number = models.IntegerField()

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name()
    
    
class Menu(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=2000,default='')
    image = models.ImageField(upload_to='menu_item/',default='menu_item/default_image.jpg')

    def __str__(self):
        return self.name