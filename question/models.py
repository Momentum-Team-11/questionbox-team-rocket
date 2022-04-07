from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from datetime import datetime

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Question(models.Model):
    pass

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

class Answer(models.Model):
    pass

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

        
        
# ===================================================================== Ref
# class Movie(models.Model):
#     title = models.CharField(max_length=200)
#     created = models.DateTimeField(default=datetime.now, verbose_name='date created')
#     watched = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='movie_user')
#     slug = models.SlugField(max_length=100,null=True, blank=True, unique=True)

#     def __str__(self):
#         return self.name

#     def save(self):
#         self.slug = slugify(self.name)
#         super().save()

# class List(models.Model):
#     name = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='list_user')
#     slug = models.SlugField(max_length=100,null=True, blank=True, unique=True)

#     def __str__(self):
#         return self.name

#     def save(self):
#         self.slug = slugify(self.name)
#         super().save()

# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='category_user')
#     slug = models.SlugField(max_length=100,null=True, blank=True, unique=True)
#     list = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True, related_name='list_list')

#     def __str__(self):
#         return self.name

#     def save(self):
#         self.slug = slugify(self.name)
#         super().save()