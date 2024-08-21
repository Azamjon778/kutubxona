from django.db import models

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    mualif = models.SmallIntegerField()
    janr = models.CharField(max_length=10)
    beti = models.SmallIntegerField()

    def __str__(self):
        return f"{self.nom}, {self.mualif}"

class Kutibxonachi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    userNAME = models.CharField(max_length=30)
    password = models.SmallIntegerField()
    def __str__(self):
        return f"{self.ism}, {self.yosh}"

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yoshi = models.SmallIntegerField()
    trik = models.BooleanField()
    def __str__(self):
        return f"{self.ism}, {self.yoshi}"

class Oquvchi(models.Model):
    ism = models.CharField(max_length=30)
    h_raqami = models.SmallIntegerField()
    sinf = models.SmallIntegerField()

    def __str__(self):
        return f"{self.ism}, {self.h_raqami}"

class Kutubxona(models.Model):
    Oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    Kitob_nomi = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    Olgan_sana = models.DateField()
    Qaytarish_sana = models.DateField()
    Qaytardimi = models.BooleanField()
    Kutubxonachi = models.ForeignKey(Kutibxonachi, on_delete=models.CASCADE)
  
    def __str__(self):
        return f"{self.Oquvchi}, {self.Kitob_nomi}"
