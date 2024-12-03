from django.db import models

from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class TodoLIst(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(default=datetime.now())

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return  self.title

    class Meta:
        ordering = ['-created']