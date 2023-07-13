from django.db import models
from .questions import userQuestions

class userChoice(models.Model):
    question = models.ForeignKey(userQuestions, on_delete=models.CASCADE, blank=True)
    choice = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
            verbose_name = "userChoice"
            verbose_name_plural = "Choices"

    def __str__(self):
        return f'{self.question}'