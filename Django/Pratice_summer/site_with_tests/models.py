from django.db import models


# Create your models here.

class Table_of_tests(models.Model):
    num_of_test = models.AutoField(pri)
    content = models.TextField(blank=True)
    id_of_test = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
