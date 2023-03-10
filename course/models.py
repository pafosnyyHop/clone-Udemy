from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from languages.fields import LanguageField


User = get_user_model()


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course')
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='courses')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()
    lang = LanguageField(max_length=10)
