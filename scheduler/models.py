from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    schedule = models.CharField(max_length=255)  # e.g., "every Monday at 10:00 AM"
    is_active = models.BooleanField(default=True)

    interval_type = models.CharField(max_length=50, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily')
    interval_value = models.IntegerField(default=1)  # Number of days/weeks/months
    custom_attributes = models.JSONField(default=dict, blank=True)  # Store any custom job attributes



    # schedule = models.JSONField()  # Store schedule details as JSON
    # interval = models.CharField(max_length=255)  # e.g., 'every Monday', 'daily', etc.
    # job_type = models.CharField(max_length=255, choices=[('email', 'Email Notification'), ('compute', 'Number Crunching')])

    def __str__(self):
        return self.name