# Generated by Django 4.1.7 on 2023-03-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_is_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
    ]
