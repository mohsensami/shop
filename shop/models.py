from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from accounts.models import User



class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug,])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField()
    description = RichTextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.slug,])
