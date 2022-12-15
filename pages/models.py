from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField



class Page(models.Model):
    STATUS_CHOICES = (
		('d', 'Draft'),		 # draft
		('p', "Publish"),		 # publish
	)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField()
    text = RichTextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title