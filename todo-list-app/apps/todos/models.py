from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class ToDoItem(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50, null=True, blank=True)
    priority = models.IntegerField(default=0)

    is_done = models.BooleanField(default=False)

    user = models.ForeignKey(User)

    def __unicode__(self):
        done = 'done' if self.is_done else 'not done'
        return '"{0}" is {1}'.format(self.name, done)
