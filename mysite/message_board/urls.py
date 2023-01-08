from django.urls import path

from . import views

urlpatterns = [
    # e.g.: /home/
    path('', views.index, name='index'),
    path('rick_roll/', views.rick_roll, name='rick_roll'),
    path('selection/', views.selection, name='selection'),
]

