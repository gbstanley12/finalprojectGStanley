from django.db import models
from django.utils import timezone

class TextSubmission(models.Model):
    title = models.CharField(max_length=200)
    submission_text = models.TextField()
    word_count = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
    # Fields for readability scores
    flesch_reading_ease = models.FloatField(null=True, blank=True)
    # ... other readability scores fields
