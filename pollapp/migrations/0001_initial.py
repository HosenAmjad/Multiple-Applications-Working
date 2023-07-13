# Generated by Django 4.1.7 on 2023-04-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('question_desc', models.CharField(max_length=255)),
                ('register_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'userQuestions',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='userChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=250)),
                ('votes', models.IntegerField(default=0)),
                ('register_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pollapp.userquestions')),
            ],
            options={
                'verbose_name': 'userChoice',
                'verbose_name_plural': 'Questions Choice',
            },
        ),
    ]
