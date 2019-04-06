# -*- coding: utf-8 -*-
# pylint: disable=

from django.contrib import admin

from backend import models

admin.site.register(models.TaskItem)
