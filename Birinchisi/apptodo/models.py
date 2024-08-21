from django.db import models

class Todotime(models.Model):
    vaqit = models.DateField()

    def __str__(self):
        return f"{self.vaqit}"

class Tododescription(models.Model):
    malumot = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.malumot}"

class Todostatus(models.Model):
    faol = models.BooleanField()

    def __str__(self):
        return f"{self.faol}"
