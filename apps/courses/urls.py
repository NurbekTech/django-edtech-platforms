from django.urls import path
from apps.courses import views

urlpatterns = [path("", views.courses, name="courses")]
