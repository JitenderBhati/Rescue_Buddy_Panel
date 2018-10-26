from django.db import models

# Create your models here.
class loginData(models.Model):
    _id = models.CharField(max_length = 100, blank=False)
    email = models.EmailField(blank = False)
    contact = models.CharField(max_length=12, blank = False)
    gender = models.CharField(max_length= 6, blank = False)
    age = models.PositiveSmallIntegerField(blank = False)
    name = models.CharField(max_length =50, blank = False)
    longitude = models.FloatField(blank=False)
    latitide = models.FloatField(blank = False)

    def __str__(self):
        return self.name + " (" + self.email + ")"

    class Meta:
        verbose_name_plural = "Login Data"

