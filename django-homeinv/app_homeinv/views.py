from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django import forms
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
    fields = ['name', 'description', 'photo', 'groups']


class ItemDeleteView(generic.DeleteView):
    model = models.Item
    success_url = reverse_lazy('index')


class ItemListView(generic.ListView):
    model = models.Item


class ParentMixin():
    def get_success_url(self):
        return getattr(self.object, self.parent_field).get_absolute_url()


class ParentCreateView(
    ParentMixin,
    SingleObjectTemplateResponseMixin,
    generic.edit.BaseCreateView
):
    parent_field = None

    template_name_suffix = '_form'

    def get_initial(self):
        return {
            self.parent_field: self.kwargs['pk']
        }

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields[self.parent_field].widget = forms.HiddenInput()
        return form


class ItemPlacedCreateView(ParentCreateView):
    template_name = 'form.html'
    model = models.ItemPlaced
    parent_field = 'item'
    fields = ['item', 'description', 'count']


class ItemPlacedUpdateView(generic.UpdateView):
    template_name = 'form.html'
    model = models.ItemPlaced
    fields = ['item', 'description', 'count']


class ItemPlacedDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    model = models.ItemPlaced
    fields = ['item', 'description', 'count']
    
    def get_success_url(self):
        return self.object.item.get_absolute_url()
