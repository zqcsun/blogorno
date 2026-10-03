from django.urls import path
from . import views
urlpatterns = [
    path("",views.lists_page,name='list_url'),
    path("<str:slug>/<int:id>/",views.item_page,name = 'item_url'),
]