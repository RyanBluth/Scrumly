__author__ = 'ryan'

from django.db import models


# Base user class
class User(models.Model):
    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    # Django adds email validation for us
    email = models.EmailField()

    def __str__(self):
        return ' '.join([
            self.email,
            self.last_name,
            self.first_name
        ])