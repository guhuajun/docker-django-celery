# -*- coding: utf-8 -*-
# pylint: disable=

'''Backend Models'''

from django.db import models


class TaskItem(models.Model):
    '''Task Item'''

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
