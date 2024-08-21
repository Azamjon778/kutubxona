from django.db import models

class Futbol(models.Model):
    ism = models.CharField(max_length=30)
    tranfer_narx = models.SmallIntegerField()
    yosh = models.SmallIntegerField()
    klub = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ism}, {self.tranfer_narx}"

class Moshina(models.Model):
    Rusum = models.CharField(max_length=25)
    kompaniya= models.CharField(max_length=30)
    raqami = models.SmallIntegerField()
    yili = models.DateField()
    rangi = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Rusum}, {self.kompaniya}"

class Maxsulot(models.Model):
    nom = models.CharField(max_length=30)
    brend = models.CharField(max_length=25)
    chegrma = models.SmallIntegerField(null=True)
    mavjud = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.nom}, {self.chegrma}"

class Kurs(models.Model):
    nom = models.CharField(max_length=30)
    yonalish = models.CharField(max_length=25)
    daraja = models.SmallIntegerField()
    davomiyligi = models.SmallIntegerField()

    def __str__(self):
        return f"{self.nom}, {self.yonalish}"

