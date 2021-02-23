from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...fixtures.fixtures import mock_superuser, mock_template
from django.db.utils import IntegrityError
from ...models import FileTemplate, Location
from ai.config import OCR_LOCATIONS, ORC_second_page


class Command(BaseCommand):
    help = "create locations from list of tuples"

    template_id = 1
    locations = OCR_LOCATIONS

    def handle(self, *args, **options):
        template = FileTemplate.objects.get(id=self.template_id)
        for location in self.locations:
            loc = Location.objects.create_location(
                template=template,
                location=location,
                description=f'Location for template {template.file.name}'
            )
            print(f'Created location entity {loc.id}')
