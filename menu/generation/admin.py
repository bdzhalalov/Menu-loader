from django.contrib import admin

from .models import Category, Menu


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ['title', 'id']
    list_filter = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu)
