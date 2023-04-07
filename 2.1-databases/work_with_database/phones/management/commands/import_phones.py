import csv

from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.reader(file, delimiter=';')

            next(phones)

            for p in phones:
                new_phone = Phone.objects.create(
                    id = int(p[0]),
                    name = p[1],
                    image = p[2],
                    price = int(p[3]),
                    release_data = p[4],
                    lte_exists = p[5],
                    slug = slugify(p[1]),
                )
            

