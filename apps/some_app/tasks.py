from __future__ import absolute_import

from django.conf import settings



# The @shared_task decorator lets you create tasks without having any concrete app instance:
@shared_task
def add(x, y):
    """
    You can import this example task as: from core.tasks import add
    You can call it as: add.delay(23, 56)
    """
    return x + y
