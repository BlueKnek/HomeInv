from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models


# Group views

class GroupCreateView(generic.CreateView):
    model = models.Group
    fields = ['name', 'description', 'photo']


class GroupDetailView(generic.DetailView):
    model = models.Group


class GroupUpdateView(generic.UpdateView):
    model = models.Group
    fields = ['name', 'description', 'photo']


class GroupDeleteView(generic.DeleteView):
    model = models.Group
    success_url = reverse_lazy('index')


class GroupListView(generic.ListView):
    model = models.Group


# Item views

class ItemCreateView(generic.CreateView):
    model = models.Item
    fields = ['name', 'description', 'photo', 'groups']


class ItemDetailView(generic.DetailView):
    model = models.Item


class ItemUpdateView(generic.UpdateView):
    model = models.Item
    fields = ['name', 'description', 'photo']


class ItemDeleteView(generic.DeleteView):
    model = models.Item
    success_url = reverse_lazy('index')


class ItemListView(generic.ListView):
    model = models.Item
