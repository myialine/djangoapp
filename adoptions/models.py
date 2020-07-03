from django.db import models


# Create your models here.

class Pet(models.Model):
    # This is a constant for the sex field. it always comes in tuples of a key for storage and a word for display value.
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    # Using choices to define model contents. Blank is true 'cause sometimes we don't know the sex of a pet.
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    # Sometimes we don't know the age of a pet. Null instead of blank means empty instead of zero because IntegerField.
    age = models.IntegerField(null=True)
    submission_date = models.DateTimeField()
    # a many-to-may relationship with the class Vaccine
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # this tells python to change the default representation of vaccine to its name.
    def __str__(self):
        return self.name
