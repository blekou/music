from django.db import models

# Create your models here.
class Tag(models.Model):

    nom =models.CharField(max_length=225)
    description =models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie article'
        verbose_name_plural = 'Categorie articles'

    def __str__(self):
        return self.nom


class CategorieArticle(models.Model):

    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/CategorieArticle")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie article'
        verbose_name_plural = 'Categorie articles'

    def __str__(self):
        return self.nom


class Article(models.Model):

    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    image = models.ImageField(upload_to="images/Article")
    tag = models.ManyToManyField(Tag, related_name='tag_Article')
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name='categorie_Article')


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.titre


class Commentaire(models.Model):

    nom = models.CharField(max_length=255)
    prenom = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='commentaire_article')
    commentaire= models.TextField()


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'commentaire '
        verbose_name_plural = 'commentaires'

    def __str__(self):
        return self.nom
