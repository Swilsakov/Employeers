from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name
