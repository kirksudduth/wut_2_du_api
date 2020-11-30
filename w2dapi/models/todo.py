from django.db import models
from .doer import Doer


class ToDo(models.Model):

    doer = models.ForeignKey(Doer, on_delete=models.DO_NOTHING)
    task = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'{self.doer} wants to {self.wut}'
