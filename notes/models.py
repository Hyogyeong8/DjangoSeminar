from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_note = models.ForeignKey(Note, on_delete=models.CASCADE, default=None, blank=True)