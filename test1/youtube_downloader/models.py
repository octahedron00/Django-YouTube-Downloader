import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class DownloadedFile(models.Model):
    address = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.created_time) + " created, " + str(self.address)

    def is_valid(self):
        return self.created_time.timestamp() >= (timezone.now() - datetime.timedelta(hours=3)).timestamp()



