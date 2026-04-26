from django.urls import path
from apps.courses import views

app_name = "courses"

urlpatterns = [
    path("", views.courses, name="courses"),
    path("<slug:slug>/", views.courses_detail, name="courses_detail"),
    path("course/<slug:slug>/", views.course_detail, name="course_detail"),
    path("lesson/<slug:slug>/", views.lesson_detail, name="lesson_detail"),
]
