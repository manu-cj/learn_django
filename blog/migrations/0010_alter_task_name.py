# Generated by Django 5.1.2 on 2024-10-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_task_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]