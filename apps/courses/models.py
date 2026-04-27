from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    """Категория — Робототехника, Программалау, т.б."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def courses_count(self):
        return self.courses.count()

    def get_absolute_url(self):
        return reverse("courses:courses_detail", kwargs={"slug": self.slug})


class Course(models.Model):
    """Курс — Arduino, ESP32, т.б."""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})


class Lesson(models.Model):
    """Сабақ — нақты бір тақырып"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"slug": self.slug})
