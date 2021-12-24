from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showUploadPage, name="upload"),
    path('select', views.uploadValidate, name="select")
]