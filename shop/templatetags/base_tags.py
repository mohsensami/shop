from django import template

from shop.models import Category, Product


register = template.Library()

@register.simple_tag
def favourite_count(user):
    if user.id:
        favourite_count = user.favourites.count()
        return favourite_count
    return '0'

@register.inclusion_tag('shop/partials/category_navbar.html')
def category_navbar():
    return {
        "categories": Category.objects.filter(is_sub=False)
    }
