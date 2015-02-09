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


class Project(models.Model):
    title = models.CharField(
        max_length=255
    )

    users = models.ManyToManyField(User)


class Iteration(models.Model):
    title = models.CharField(
        max_length=255
    )

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    project = models.ForeignKey(Project)


class Category(models.Model):
    title = models.CharField(
        max_length=255
    )

    iteration = models.ForeignKey(Iteration)


class Task(models.Model):
    title = models.CharField(
        max_length=255
    )

    description = models.CharField(
        max_length=5000
    )

    category = models.ForeignKey(Category)

    assignee = models.ForeignKey(User)



