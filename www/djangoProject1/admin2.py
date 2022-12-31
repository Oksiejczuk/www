from django.db import models

class Admin(models.Model):
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    wiek = models.IntegerField(default=0)
    adres = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    telefon = models.IntegerField(default=0)
    zarobki = models.IntegerField(default=0)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Klient(models.Model):
    imie = models.CharField(max_length=64)
    nazwisko = models.CharField(max_length=64)
    wiek = models.IntegerField(default=0)
    adres = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    telefon = models.IntegerField(default=0)
    dane_platnosci  = models.CharField(max_length=64)
    login = models.CharField(max_length=64)

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Wynajem(models.Model):
    model = models.CharField(max_length=64)
    cena = models.IntegerField(default=0)
    marka = models.CharField(max_length=64)
    rocznik = models.IntegerField(default=0)
    data_wynajmu = models.IntegerField(default=0)


    def __str__(self):
        return self.model + " " + self.cena

class Zwrot(models.Model):
    stan_auta = models.CharField(max_length=64)
    data_zwrotu = models.IntegerField(default=0)
    warunki_zwrotu = models.CharField(max_length=64)

    def __str__(self):
        return self.stan_auta + " " + self.data_zwrotu

class Auta(models.Model):
    model = models.CharField(max_length=64)
    cena = models.IntegerField(default=0)
    marka = models.CharField(max_length=64)
    rocznik = models.IntegerField(default=0)

    def __str__(self):
        return self.model + " " + self.cena
