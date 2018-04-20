from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

def __str__(self):
    return self.title