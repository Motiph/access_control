from django.db import models
from .mixins import TimeStampModel


class AllowedHost(TimeStampModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return "Allowed host: {}".format(self.name)


class WhiteListItem(TimeStampModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return "White list item: {}".format(self.name)
