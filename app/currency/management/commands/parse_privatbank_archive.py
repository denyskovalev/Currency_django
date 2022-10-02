from django.core.management.base import BaseCommand, CommandError
from currency.models import Rate


class Command(BaseCommand):
    help = 'Closes the specified pool for voting'

    def handle(self, *args, **options):
        print(f'Rates count:', Rate.objects.count())