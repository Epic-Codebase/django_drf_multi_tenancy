from django.db import models

class Hotel(models.Model):
    '''
    Sample model tenant-specif
    '''
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField() 
    picture = models.ImageField(upload_to="hotel_pictures/", blank=True, null=True)

    def __str__(self):
        return self.name
