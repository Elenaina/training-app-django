from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django import forms

from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    position = models.ForeignKey('Position', on_delete=models.PROTECT)
    employed_since = models.DateTimeField(default=timezone.now)
    salary = models.DecimalField(max_digits=19, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True)
    is_present = models.BooleanField()
    leave_left = models.IntegerField(default=20)

    def __str__(self):
        return self.name + ' ' + self.surname


class Position(models.Model):
    position_name = models.CharField(max_length=200)
    position_desc = models.TextField()
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=1)

    def clean(self, *args, **kwargs):
        if self.salary_max < self.salary_min:
            raise forms.ValidationError("Maximum salary should be greater than its minimum")

        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.position_name
