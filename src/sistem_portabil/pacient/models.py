from django.db import models


class Pacient(models.Model):
    nume = models.CharField(max_length=200, null=False, blank=False, default='')
    prenume = models.CharField(max_length=200, null=False, blank=False, default='')
    varsta = models.IntegerField(blank=True, null=True)
    cnp = models.CharField(max_length=15, null=False, blank=False, default='')
    numar_telefon = models.CharField(max_length=15, null=True, blank=True)
    profesie = models.CharField(max_length=200, null=True, blank=True)
    loc_munca = models.CharField(max_length=200, null=True, blank=True)
