from django.db import models
from django.contrib.auth.models import User
from sistem_portabil.pacient.models import Pacient, Recomandari, DateMedicale, Adresa


class RecomandariPacient(models.Model):
    class Meta:
        verbose_name = 'Recomandari Pacient'
        verbose_name_plural = 'Recomandari Pacient'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    recomandari = models.ForeignKey(Recomandari, on_delete=models.CASCADE)

    def __str__(self):
        return self.pacient.nume


class DateMedicalePacient(models.Model):
    class Meta:
        verbose_name = 'Date Medicale Pacient'
        verbose_name_plural = 'Date Medicale Pacient'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    date_medicale = models.ForeignKey(DateMedicale, on_delete=models.CASCADE)

    def __str__(self):
        return self.pacient.nume


class AvertizarePacient(models.Model):
    class Meta:
        verbose_name = 'Avertizare Pacient'
        verbose_name_plural = 'Avertizare Pacient'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Doctor')
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    avertizare = models.CharField(max_length=255)

    def __str__(self):
        return self.pacient.nume



class AdresaPacient(models.Model):
    adresa = models.ForeignKey(Adresa, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)