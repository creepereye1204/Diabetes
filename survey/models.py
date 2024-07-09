from django.db import models


class Survey(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Data(models.Model):

    pregnancies = models.IntegerField(default=0)
    glucose = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    skin_thickness = models.IntegerField(default=0)
    insulin = models.IntegerField(default=0)
    bmi = models.IntegerField(default=0)
    diabetes_pedigree_function = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    outcome = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)
