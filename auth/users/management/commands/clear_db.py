from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Clear all data from the database'

    def handle(self, *args, **kwargs):
        for model in apps.get_models():
            model.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All data has been cleared from the database'))
