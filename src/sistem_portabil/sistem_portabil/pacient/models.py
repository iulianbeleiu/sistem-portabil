from django.db import models
from django.contrib.auth.models import User


class Pacient(models.Model):
    class Meta:
        verbose_name = 'Pacient'
        verbose_name_plural = 'Pacienti'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor', related_name='user')
    user_pacient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_pacient', unique=True)
    nume = models.CharField(max_length=200, null=False, blank=False, default='')
    prenume = models.CharField(max_length=200, null=False, blank=False, default='')
    varsta = models.IntegerField(blank=True, null=True)
    cnp = models.CharField(max_length=15, null=False, blank=False, default='')
    numar_telefon = models.CharField(max_length=15, null=True, blank=True)
    profesie = models.CharField(max_length=200, null=True, blank=True)
    loc_munca = models.CharField(max_length=200, null=True, blank=True)
    adresa = models.ForeignKey('Adresa', on_delete=models.CASCADE, null=True, blank=True)
    date_medicale = models.ForeignKey('DateMedicale', on_delete=models.CASCADE, null=True, blank=True)
    recomandari = models.ForeignKey('Recomandari', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nume


class DateMedicale(models.Model):
    class Meta:
        verbose_name = 'Date Medicale'
        verbose_name_plural = 'Date Medicale'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    istoric_medical = models.TextField(blank=True, null=True, default='')
    alergii = models.TextField(blank=True, null=True, default='')
    consultatii_cardiologice = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return f"Alergii: {self.alergii}; Consultatii Cardiologice: {self.consultatii_cardiologice}"


class Recomandari(models.Model):
    class Meta:
        verbose_name = 'Recomandari'
        verbose_name_plural = 'Recomandari'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    tip_recomandare = models.CharField(max_length=300, blank=True, null=True, default='')
    durata_zilnica = models.IntegerField()
    alte_indicatii = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return f"{self.tip_recomandare} {self.durata_zilnica} {self.alte_indicatii}"


class Adresa(models.Model):
    class Meta:
        verbose_name = 'Adresa'
        verbose_name_plural = 'Adrese'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    tara = models.CharField(max_length=200, null=False, blank=False)
    judet = models.CharField(max_length=200, null=False, blank=False)
    localitate = models.CharField(max_length=200, null=False, blank=False)
    strada = models.CharField(max_length=200, null=False, blank=False)
    scara = models.CharField(max_length=200, null=True, blank=True, default='')
    numar = models.CharField(max_length=200, null=False, blank=False)
    apartament = models.CharField(max_length=200, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.tara} {self.judet} {self.localitate}"

