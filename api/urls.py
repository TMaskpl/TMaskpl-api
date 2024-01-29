from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIData.getData),
    path('add/',views.APIData.addItem)
]
