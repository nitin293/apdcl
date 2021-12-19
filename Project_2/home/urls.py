
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.button),
    path('output', views.output,name="script")
]
