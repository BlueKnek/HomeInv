from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models


class ItemCreateView(generic.CreateView):
    model = models.Item
    fields = ['name', 'description', 'photo']


class ItemDetailView(generic.DetailView):
    model = models.Item


class ItemUpdateView(generic.UpdateView):
    model = models.Item
    fields = ['name', 'description', 'photo']


class ItemDeleteView(generic.DeleteView):
    model = models.Item
    success_url = reverse_lazy('index')

