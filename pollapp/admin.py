from django.contrib import admin

# Register your models here.
from pollapp.models.choices import userChoice
from pollapp.models.questions import userQuestions


class NewQuestionsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "question_desc", "register_on"]

    class Meta:
        model=userQuestions
admin.site.register(userQuestions, NewQuestionsAdmin)


class NewChoiceAdmin(admin.ModelAdmin):
    list_display = ["__str__", "choice", "votes", "register_on"]

    class Meta:
        model=userChoice
admin.site.register(userChoice, NewChoiceAdmin)
