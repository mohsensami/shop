from django.contrib import admin
from .models import Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']

admin.site.register(Page, CategoryAdmin)
