from django.db import models


class Company(models.Model):
    max_length_company_name = 50

    name = models.CharField('name', max_length=max_length_company_name)

    def __str__(self):
        return self.name