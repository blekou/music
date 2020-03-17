from django.db import models

# Create your models here.

class InfoSite(models.Model):

    nom = models.CharField(max_length=225)
    mapurl=models.URLField()
    email=models.EmailField()
    logo = models.ImageField(upload_to='images/InfoSite')

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "InfoSite"
        verbose_name_plural = "InfoSites"

    def __str__(self):
        return self.nom


class CompteSocial(models.Model):

    ICONE = [
        ("facebook", "fa-facebook"),
        ("googleplus", "fa-googleplus"),
        ("instagram", "fa-instagram"),
        ("linkedin", "fa-linkedin"),
    ]

    icones =models.CharField(choices = ICONE,max_length=30)
    lien= models.URLField()
    nom=models.CharField(max_length=225)

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "CompteSocial"
        verbose_name_plural = "CompteSocials"

    def __str__(self):
        return self.nom


class Presentation(models.Model):


    nom = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to='images/Presentation')
    video = models.TextField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Presentation"
        verbose_name_plural = "Presentations"

    def __str__(self):
        return self.nom


class Temoignage(models.Model):


    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='images/Temoignage')
    message = models.TextField()

    date_add = models.DateTimeField(auto_now = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "temoignage"
        verbose_name_plural = "temoignages"

    def __str__(self):
        return self.nom
