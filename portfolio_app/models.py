from django.db import models


class Drawing(models.Model):
    url = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name_plural = 'drawings'
