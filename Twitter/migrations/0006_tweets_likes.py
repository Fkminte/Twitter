# Generated by Django 3.2.18 on 2023-04-23 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Twitter', '0005_alter_tweets_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
