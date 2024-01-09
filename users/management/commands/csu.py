from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            name='superuser'
        )

        user.set_password('ad123min')
        user.save()
        