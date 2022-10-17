from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from enum import unique



class Thing(models.Model):
    name = models.TextField(max_length=30, unique = True, blank = False)
    description = models.TextField(max_length =120,blank =True)
    quantity = models.TextField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
