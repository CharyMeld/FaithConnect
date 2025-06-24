from django.db import models
from django.conf import settings

class Post(models.Model):
    content = models.TextField()
    media_files = models.FileField(upload_to='uploads/', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.author.username} at {self.created_at.strftime("%Y-%m-%d %H:%M")}'

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='post_files/')

    def __str__(self):
        return f'File for Post {self.post.id}'

