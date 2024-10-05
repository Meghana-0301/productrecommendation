import random
from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Populate the database with random products'

    def handle(self, *args, **kwargs):
        product_names = ['Product 1', 'Product 2', 'Product 3' ]
        for name in product_names:
            Product.objects.create(
                name=name,
                price=random.uniform(10.0, 100.0),
                description=f'Description for {name}'
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated products'))
