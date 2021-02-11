from django.db import models
from typing import List, Tuple

from .file_template import FileTemplate
from .field_coordinate import FieldCoordinate
from .keyword import Keyword
from ai.config import OCRLocation


class LocationManager(models.Manager):

    def create_location(self, template: FileTemplate, location: tuple, description: str = None):
        coordinate_entity = FieldCoordinate(
            x=location.bbox[0],
            y=location.bbox[1],
            width=location.bbox[2],
            height=location.bbox[3]
        )
        coordinate_entity.save()
        location_entity = Location(
            id=location.id,
            coordinates=coordinate_entity,
            to_template=template,
            description=description,
        )
        location_entity.save()
        for keyword in location.filter_keywords:
            keyword_entity = Keyword(
                keyword=keyword,
                to_location=location_entity
            )
            keyword_entity.save()
        return location


class Location(models.Model):
    id_max_len = 100

    id = models.CharField('id', max_length=id_max_len, primary_key=True)
    coordinates = models.ForeignKey(FieldCoordinate, on_delete=models.CASCADE)
    to_template = models.ForeignKey(FileTemplate, on_delete=models.CASCADE)

    description = models.CharField(
        'description',
        max_length=id_max_len,
        help_text="Just to know for which template this location is",
        null=True,
        blank=True
    )

    objects = LocationManager()

    def get_location_tuple(self):
        keywords = list(self.keyword_set.all().values_list('keyword', flat=True))
        coord = self.coordinates.get_coordinates()
        return OCRLocation(self.id, coord, keywords)
