# Generated by Django 5.1.2 on 2024-10-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='part',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
