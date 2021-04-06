from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "creates locations and populates by entities with mock data"

    def handle(self, *args, **options):
        call_command('migrate')
        call_command('populate')
