from django.db import models

class ProcessedURL(models.Model):
    url = models.URLField(unique=True)
    is_scanned_for_virus = models.BooleanField(default=False)
    is_duplicated = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    processed_order = models.PositiveIntegerField(unique=True, blank=True, null=True, default=0)

    def __str__(self):
        return self.url
