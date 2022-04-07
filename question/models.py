from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField, DateTimeField
from django.template.defaultfilters import slugify
from datetime import datetime

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Question(models.Model):
    title = models.TextField()
    question = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=datetime.now)
    user = models.ForeignKey(User, related_name=("question_user"), on_delete=models.CASCADE)
    favorited = models.ManyToManyField(User, related_name=("question_favorited"))

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()

class Answer(models.Model):
    answer = CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=datetime.now)
    question = models.ForeignKey(Question, related_name='answer_to_question', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name=("answer_user"), on_delete=models.CASCADE)
    favorited = models.ManyToManyField(User, related_name=("answer_favorited"))
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super().save()
