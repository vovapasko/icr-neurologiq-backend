from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...fixtures.fixtures import mock_superuser, mock_template
from django.db.utils import IntegrityError
from ...models import FileTemplate, Company


class Command(BaseCommand):
    help = "populates by entities with mock data"

    def handle(self, *args, **options):
        self.__create_superuser()
        self.__create_company()

    def __create_superuser(self):
        try:
            User.objects.create_superuser(
                **mock_superuser
            )
            self.print(f"Superuser created!")
        except IntegrityError:
            self.print("Such a user already exists!")

    def print(self, message: str):
        self.stdout.write(message)

    def __create_company(self):
        company = Company(name='bank 1')
        self.print("Mock company created!")
        company.save()
