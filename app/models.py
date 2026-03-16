from django.db import models


class Contact(models.Model):
    name = models.CharField()
    course = models.CharField(null=True, blank=True)
    phone_number = models.CharField()

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField()
    phone_number = models.CharField()
    def __str__(self):
        return self.name
class Kurslar(models.Model):
    image = models.ImageField()
    title = models.CharField()
    information = models.TextField()
class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField()
    author = models.CharField()
    image_author = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title  # Было self.name, что и вызывало ошибку
