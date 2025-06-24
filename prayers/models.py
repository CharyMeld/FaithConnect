from django.db import models
from django.conf import settings


class PrayerRequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='prayer_requests',
        null=True,  # Allow anonymous submissions
        blank=True
    )
    name = models.CharField(max_length=255, default='Anonymous')
    email = models.EmailField(default='example@example.com')
    title = models.CharField(max_length=255, blank=True)  # Optional title
    message = models.TextField()
    is_prayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.title or self.name} by {self.user.username}"
        return f"{self.title or self.name} - {self.created_at.strftime('%Y-%m-%d')}"

class PrayerResponse(models.Model):
    prayer_request = models.ForeignKey(
        PrayerRequest, 
        on_delete=models.CASCADE, 
        related_name='responses'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='prayer_responses'
    )
    message = models.TextField()
    is_private = models.BooleanField(default=False)  # Private response only visible to request owner?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.sender.username} to '{self.prayer_request.title}'"
