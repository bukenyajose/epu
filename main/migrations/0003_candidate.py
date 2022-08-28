# Generated by Django 4.1 on 2022-08-27 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_blog_thumbnail_alter_member_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='', max_length=255)),
                ('year', models.CharField(default='', max_length=255)),
                ('elected', models.BooleanField(default=False)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.member')),
            ],
        ),
    ]