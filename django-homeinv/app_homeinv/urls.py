from django.urls import path

from . import views

app_name = 'app_homeinv'

urlpatterns = [
    path('item/create', views.ItemCreateView.as_view(), name='item-create'),
    path('item/<pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/<pk>/update', views.ItemUpdateView.as_view(), name='item-update'),
    path('item/<pk>/delete', views.ItemDeleteView.as_view(), name='item-delete')
]

