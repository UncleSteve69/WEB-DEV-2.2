from django.urls import path, include
from about_us import views

urlpatterns = [
    path('about_us/', views.about_us)
]