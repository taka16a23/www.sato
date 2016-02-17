from __future__ import unicode_literals

from django.db import models

# Create your models here.
CATEGORIES = (
    (1, 'feature'),
    (2, 'fix'),
)

PRIORITIES = ((5, 'high'),
              (10, 'normal'),
              (15, 'low'))


class TodoEntryModel(models.Model):
    r"""TodoEntryModel

    TodoEntryModel is a models.Model.
    Responsibility:
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=1)
    priority = models.IntegerField(choices=PRIORITIES, default=10)
    finished = models.BooleanField(default=False)
