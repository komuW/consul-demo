from django.conf import settings
from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate


def create_intial_superuser():
    """
    create an intial superuser.
    """
    try:
        if settings.STAGE != "production":
            user, created = User.objects.get_or_create(username='kill')
            user.set_password('kill')
            user.is_superuser = True
            user.is_staff = True
            user.first_name = user.last_name= 'kill'
            user.email = 'kill@example.com'
            user.save()
    except Exception as e:
        pass

create_intial_superuser()
