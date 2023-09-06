from django.core.management import BaseCommand
from shopaap.models import Orders
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username='admin')
        order = Orders.objects.get_or_create(
            delivery_address='ul Pushkina dom Kolotushkina',
            promocode='sale123',
            user=user,
        )
        self.stdout.write(f"Created order {order}")
