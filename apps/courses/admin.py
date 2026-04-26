from django.contrib import admin
from .models import Category, Course, Lesson


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "courses_count"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "slug"]
    list_filter = ["category"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "order"]
    list_filter = ["course"]
    ordering = ["course", "order"]
    prepopulated_fields = {"slug": ("title",)}
