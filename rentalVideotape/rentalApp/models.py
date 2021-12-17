from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField(range(1, 200))
    date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Status(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Videotape(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    released = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    director = models.ForeignKey(Director, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')
    description = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class Rental(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    id = models.IntegerField(primary_key=True)
    videotape = models.ForeignKey(Videotape, on_delete=models.PROTECT, unique=True)
    date_start = models.DateField()
    date_end = models.DateField()
    buyer_name = models.CharField(max_length=50)
    buyer_surname = models.CharField(max_length=50)
    buyer_email = models.EmailField()
    buyer_phone = models.CharField(validators=[phoneNumberRegex], max_length=16)
