from django.db import models


class Drawing(models.Model):
    url = models.CharField(max_length=200, default=None)

    class Meta:
        verbose_name_plural = 'drawings'


class PortfolioUrls(models.Model):
    resume_url = models.CharField(max_length=200, default=None)
    linkedin_url = models.CharField(max_length=100, default=None)
    github_url = models.CharField(max_length=100, default=None)
