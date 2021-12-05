from django.db import models
from django.db.models.deletion import SET_NULL

class Viloyat(models.Model):
    name = models.CharField(max_length=100)
    markazi = models.CharField(max_length=100)
    maydoni = models.CharField(max_length=100)
    axolisi = models.CharField(max_length=100)
    malumotlar = models.TextField()
    rasm = models.ImageField(upload_to ='viloyat/')

    def __str__(self):
        return self.name


# class Maskan(models.Model):
#     joy_nomi = models.CharField(max_length=100)
#     maskan_joyi = models.CharField(max_length=100)
#     image_uchun = models.CharField(max_length=100)
#     image_joy = models.CharField(max_length=100)
#     malumot = models.CharField(max_length=150)
#     boshqa = models.CharField(max_length=150)
#     narx = models.CharField(max_length=100)
#     image = models.ImageField(upload_to ='media/')

#     def __str__(self):
#         return self.joy_nomi