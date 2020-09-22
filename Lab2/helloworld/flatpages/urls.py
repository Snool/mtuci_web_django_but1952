from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.index_no_type, name='index')
]
