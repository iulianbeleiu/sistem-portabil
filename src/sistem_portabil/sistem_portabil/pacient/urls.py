
from django.urls import path, include
from . import views
from .views import test

urlpatterns = [
    path('test', views.test, name='test'),
    path('fixture', views.fixture, name='fixture'),
]