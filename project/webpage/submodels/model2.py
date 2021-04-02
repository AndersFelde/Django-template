from django.db import models
from .model1 import Model1


class Model2(models.Model):
    model1 = models.ForeignKey(Model1,
                               on_delete=models.CASCADE,
                               related_name="lag")
    id = models.IntegerField()
    text = models.CharField()

    def __str__(self):
        return self.id
