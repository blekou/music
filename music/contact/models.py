from django.db import models

# Create your models here.

class Contact(models.Model):


    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    sujet = models.TextField()
    message = models.TextField()
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Newslatter(models.Model):


    email = models.EmailField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Newslatter"
        verbose_name_plural = "Newslatters"

    def __str__(self):
        return self.email
