from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

# Custom User model
class User(AbstractUser):
    church = models.CharField(max_length=255, blank=True, null=True)
    favorite_verse = models.TextField(blank=True, null=True)
    ministry_interests = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

# BibleVerse model
class BibleVerse(models.Model):
    book = models.CharField(max_length=100)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.book} {self.chapter}:{self.verse}"

