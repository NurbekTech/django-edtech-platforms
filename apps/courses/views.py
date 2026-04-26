from django.shortcuts import render, get_object_or_404
from .models import Category, Course, Lesson


# Create your views here.
def courses(request):
    categories = Category.objects.all()
    return render(request, "courses/courses.html", {"categories": categories})


def courses_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    courses = Course.objects.filter(category=category)

    context = {
        "category": category,
        "courses": courses,
    }

    return render(request, "courses/courses_detail.html", context=context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.all()

    context = {
        "course": course,
        "lessons": lessons,
    }
    return render(request, "courses/course_detail.html", context=context)


def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)

    context = {
        "lesson": lesson,
    }
    return render(request, "courses/lesson_detail.html", context=context)
