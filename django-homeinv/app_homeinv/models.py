import json

from django.db import models
from django.urls import reverse_lazy


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='items')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy('homeinv:item-detail', kwargs={'pk': self.pk})
