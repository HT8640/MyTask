from django.urls import path
from myapp import views

urlpatterns = [
    path('images', views.image_list),
]