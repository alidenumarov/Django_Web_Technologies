from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author(models.Model):
    name = models.CharField(max_length=200, blank=True)

def __str__(self):
    return self.name

class Book(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

def __str__(self):
    return self.title

class Todo(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    priority = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
     )
    #done = models.BooleanField(default=False)

def __str__(self):
    return self.title

class Contact(models.Model):
    name = models.CharField(max_length=300, blank=True)
    number = models.IntegerField(
        default=100,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    image = models.CharField(max_length=1000, blank=True)

def __str__(self):
    return self.name