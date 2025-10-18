from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser with email'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email address')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **options):
        email = options['email']
        password = options['password']

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR(f'Error: User with email {email} already exists!'))
            return

        try:
            user = User.objects.create_superuser(
                username=email,
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True,
                is_customer=True
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created superuser: {user.email}'
                )
            )
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'Validation error: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
