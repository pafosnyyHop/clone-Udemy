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
    # LANGUAGE_CHOICES = [
    #     ('aa', ''),
    #     ('ab', ''),
    #     ('ae', ''),
    #     ('af', ''),
    #     ('ak', ''),
    #     ('am', ''),
    #     ('an', ''),
    #     ('ar', ''),
    #     ('as', ''),
    #     ('av', ''),
    #     ('ay', ''),
    #     ('az', ''),
    #     ('ba', ''),
    #     ('be', ''),
    #     ('bg', ''),
    #     ('bh', ''),
    #     ('bi', ''),
    #     ('bm', ''),
    #     ('bn', ''),
    #     ('bo', ''),
    #     ('br', ''),
    #     ('bs', ''),
    #     ('ca', ''),
    #     ('ce', ''),
    #     ('ch', ''),
    #     ('co', ''),
    #     ('cr', ''),
    #     ('cs', ''),
    #     ('cu', ''),
    #     ('cv', ''),
    #     ('cy', ''),
    #     ('da', ''),
    #     ('de', ''),
    #     ('dv', ''),
    #     ('dz', ''),
    #     ('ee', ''),
    #     ('el', ''),
    #     ('en', ''),
    #     ('eo', ''),
    #     ('es', ''),
    #     ('et', ''),
    #     ('eu', ''),
    #     ('fa', ''),
    #     ('ff', ''),
    #     ('fi', ''),
    #     ('fj', ''),
    #     ('fo', ''),
    #     ('fr', ''),
    #     ('fy', ''),
    #     ('ga', ''),
    #     ('gd', ''),
    #     ('gl', ''),
    #     ('gn', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ('', ''),
    #     ()
    # ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course')
    category_id = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='courses')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    description = models.TextField()
    lang = LanguageField(max_length=10)
