from django.db import models
import datetime

class userQuestions(models.Model):
    question_text = models.CharField(max_length=255)
    question_desc = models.CharField(max_length=255)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
            verbose_name = "userQuestions"
            verbose_name_plural = "Questions"

    def __str__(self):
        return f'{self.question_text}'

    def was_published_recently(self):
         return self.register_on >= datetime.timezone.now(days=1) -datetime.timedelta