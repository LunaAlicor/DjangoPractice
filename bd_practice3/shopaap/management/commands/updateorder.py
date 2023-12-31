from django.core.management import BaseCommand
from shopaap.models import Orders
from shopaap.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Orders.objects.first()
        if not order:
            self.stdout.write("No order found")
            return
        products = Product.objects.all()
        for product in products:
            order.products.add(product)
        order.save()
        self.stdout.write(self.style.SUCCESS(f'added products {order.products.all()} to order {order}'))
