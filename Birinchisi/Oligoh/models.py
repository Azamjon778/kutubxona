from django.db import models

class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    yonalish = models.CharField(max_length=25)
    yoshi = models.SmallIntegerField()
    fani = models.CharField(max_length=20, null=True)
    def __str__(self):
        return f"{self.ism}, {self.yonalish}"

