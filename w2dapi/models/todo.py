from django.db import models
from .doer import Doer


class ToDo(models.Model):

    doer = models.ForeignKey(Doer, on_delete=models.DO_NOTHING)
    wut = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
