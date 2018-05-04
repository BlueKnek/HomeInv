from django.urls import path

from . import views

app_name = 'app_homeinv'

urlpatterns = [
    # Group
    path('groups', views.GroupListView.as_view(), name='group-list'),
    path('group/create', views.GroupCreateView.as_view(), name='group-create'),
    path('group/<pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('group/<pk>/update', views.GroupUpdateView.as_view(), name='group-update'),
    path('group/<pk>/delete', views.GroupDeleteView.as_view(), name='group-delete'),

    # Item
    path('items', views.ItemListView.as_view(), name='item-list'),
    path('item/create', views.ItemCreateView.as_view(), name='item-create'),
    path('item/<pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/<pk>/update', views.ItemUpdateView.as_view(), name='item-update'),
    path('item/<pk>/delete', views.ItemDeleteView.as_view(), name='item-delete'),
]
