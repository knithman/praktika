from django.db import models

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Automobilio_modelis(models.Model):
    metai = models.IntegerField('Metai')
    marke = models.CharField('Markė', max_length=200)
    modelis = models.CharField('Modelis', max_length=200)
    variklis = models.CharField('Variklis', max_length=200)

    def __str__(self):
        return f"{self.metai}, {self.marke} {self.modelis}, {self.variklis}"

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilio modeliai'


class Automobilis(models.Model):
    savininkas = models.CharField(('Owner'), max_length=200)
    automobilio_modelis_id = models.ForeignKey('Automobilio_modelis', verbose_name=("Automobilis"), on_delete=models.SET_NULL, null=True)
    valstybinis_numeris = models.CharField(('ValNr'), max_length=200)
    vin_kodas = models.CharField(('VIN code'), max_length=200)

    def __str__(self):
        return f"{self.savininkas}: {self.automobilio_modelis_id}, {self.valstybinis_numeris}, {self.vin_kodas}"

    class Meta:
        verbose_name = ('Automobilis')
        verbose_name_plural = ('Automobiliai')



class Paslauga(models.Model):
    name = models.CharField('Pavadinimas', max_length=200)
    kaina = models.DecimalField('Kaina', max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'


class Uzsakymas(models.Model):
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    klientas_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField('Data', null=True, blank=True)
    @property
    def suma(self):
        uzsakymo_eilutes = UzsakymoEilute.objects.filter(uzsakymas_id=self.id)
        suma = 0
        for eilute in uzsakymo_eilutes:
            suma += eilute.kiekis * eilute.kaina
        return suma

    def __str__(self):
        return f"{self.automobilis_id}: {self.suma}"

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

    STATUS = (
        ('p', 'Patvirtinta'),
        ('v', 'Vykdoma'),
        ('a', 'Atlikta'),
        ('t', 'Atšaukta'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='p',
    )


class UzsakymoEilute(models.Model):
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")
    kaina = models.FloatField("Kaina")
    uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE)

    @property
    def suma(self):
        return self.kiekis * self.kaina

    def __str__(self):
        return f"{self.paslauga_id} – {self.kiekis}: {self.kaina} {self.suma}"

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'








