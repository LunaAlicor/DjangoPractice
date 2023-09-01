from django.core.management import BaseCommand
from shopaap.models import Product
# from models import Product


class Command(BaseCommand):
    """
    Creates product
    """

    def handle(self, *args, **options):
        self.stdout.write('Create products')
        products_names = [
            'Laptop',
            "Desktop",
            "Smartphone"
        ]
        for product_name in products_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f'Created product {product.name}')
        product.save()
        self.stdout.write(self.style.SUCCESS("Product created"))