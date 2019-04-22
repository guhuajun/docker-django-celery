# -*- coding: utf-8 -*-
# pylint: disable=


from django.db.models.signals import post_save
from django.dispatch import receiver
from celery import group, signature

from backend import models, tasks


@receiver(post_save, sender=models.TaskItem)
def start_task(*args, **kwargs):
    '''添加测试任务'''

    task_sigs = []
    for num in range(1000):
        task_sigs.append(signature(
            'backend.tasks.add', kwargs={'x':2, 'y': num}))
    group(task_sigs).apply_async()
