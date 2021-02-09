from django.db import models


class Demo(models.Model):
    nom = models.CharField(max_length=200, null=True)
    formateur = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

