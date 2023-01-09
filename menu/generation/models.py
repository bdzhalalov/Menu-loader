from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=32)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
