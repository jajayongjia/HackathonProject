from django.urls import path

from . import views

urlpatterns = [
    path('data', views.get_all_data, name='fetch all'),
]
