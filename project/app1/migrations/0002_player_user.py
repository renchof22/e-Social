# Generated by Django 2.1.2 on 2018-11-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_django', '0008_partial_timestamp'),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth'),
        ),
    ]
