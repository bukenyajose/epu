# Generated by Django 4.1 on 2022-08-27 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_member_is_external_member_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='authored_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
