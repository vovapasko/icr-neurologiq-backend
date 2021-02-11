from django.db import models


class FieldCoordinate(models.Model):
    x = models.IntegerField('x', help_text='Top left x box coordinate')
    y = models.IntegerField('y', help_text='Top left x box coordinate')
    width = models.IntegerField('width', help_text='width of the box')
    height = models.IntegerField('height', help_text='height of the box')

    def get_coordinates(self) -> tuple:
        return self.x, self.y, self.width, self.height
