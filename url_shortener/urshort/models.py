from django.db import models

# Create your models here.


class ShortUrl (models.Model):
    long_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=100)
    date_time_created = models.DateTimeField()

    def __str__(self) -> str:
        return self.long_url[0:50]
