from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Post:
    title = models.CharField(max_length= 24)
    slug = models.SlugField(max_length= 200, blank = True, null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    def __str__(self):
        return f"(self.title)-(self.id)"