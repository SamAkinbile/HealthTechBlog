# Generated by Django 5.0.7 on 2024-08-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
