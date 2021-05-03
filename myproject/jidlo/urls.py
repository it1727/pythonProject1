from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.JidloListView.as_view(), name='list'),
    path('detail/<int:pk>', views.JidloDetailView.as_view(), name='detail'),
]