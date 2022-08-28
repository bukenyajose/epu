# Generated by Django 4.1 on 2022-08-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(default='user@ecologicalpartyofuganda.com', max_length=254, unique=True),
        ),
    ]