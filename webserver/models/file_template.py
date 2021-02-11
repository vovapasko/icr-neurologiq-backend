import os

from django.db import models


# Create your models here.
class FileTemplate(models.Model):
    description_max_len = 50

    file = models.FileField(upload_to='templates/')
    description = models.CharField(
        'description',
        max_length=description_max_len,
        null=True,
        blank=True
    )
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.file.name} - {self.description}'

    def get_path(self):
        return self.file.url

    def get_locations_list(self) -> list:
        locations = list([element.get_location_tuple() for element in self.location_set.all()])
        return locations
