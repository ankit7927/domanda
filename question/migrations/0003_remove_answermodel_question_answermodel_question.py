# Generated by Django 5.0.6 on 2024-05-31 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_remove_questionmodel_answers_answermodel_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answermodel',
            name='question',
        ),
        migrations.AddField(
            model_name='answermodel',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='question.questionmodel'),
            preserve_default=False,
        ),
    ]
