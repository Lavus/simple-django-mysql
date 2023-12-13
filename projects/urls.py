# projects/urls.py

from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:source>/', views.project_index, name='project_index'),
    path('<str:source>/<int:pk>/', views.project_detail, name='project_detail')
]