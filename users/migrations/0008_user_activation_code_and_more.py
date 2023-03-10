# Generated by Django 4.1.7 on 2023-03-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='password_reset_code_created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]