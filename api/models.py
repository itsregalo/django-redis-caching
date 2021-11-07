from django.db import models

class Question(models.Model):
    author = models.CharField(max_length=100)
    question = models.TextField()

    def __str__(self):
        return self.question
    

