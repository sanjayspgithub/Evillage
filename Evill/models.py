from django.db import models
# Create your models here.
class donate_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return  self.name
class contact_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    mess= models.CharField(max_length=1000)

    def __str__(self):
        return  self.name
