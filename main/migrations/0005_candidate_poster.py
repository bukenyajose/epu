# Generated by Django 4.1 on 2022-08-27 20:51

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_candidate_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='poster',
            field=models.ImageField(blank=True, upload_to=main.models.get_upload_path),
        ),
    ]