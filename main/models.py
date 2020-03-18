from django.db import models

class Advice(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    advice = models.TextField()

    def __str__(self):
        return self.advice
