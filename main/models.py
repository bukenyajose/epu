from turtle import position
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

def get_upload_path(instance, filename):
    member = instance.member
    position = instance.position
    full_name = f"{member.first_name}{member.last_name}"
    return f"posters/{full_name}/{position.replace(' ', '_')}/{filename}"

def get_absolute_url_default(instance):
    date_str = instance.updated_at.strftime('%Y/%m/%d')
    year = int(date_str.split('/')[0])
    month = int(date_str.split('/')[1])
    day = int(date_str.split('/')[2])
    return reverse('main:blog_details', args=[year, month, day, instance.slug, instance.id])


def get_slug_name(self):
    model = self.place.name
    slug_name = model.replace(' ', '_')
    return slug_name

class Member(models.Model):
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=30)
    email = models.EmailField(blank=False, unique=True, default=f"user@ecologicalpartyofuganda.com")
    role = models.CharField(blank=False, max_length=250, default="Member")
    image = models.ImageField(upload_to="images/%Y/%m/%d/members/")
    facebook = models.URLField(default="https://www.ecologicalpartyofuganda.com")
    twitter = models.URLField(default="https://www.ecologicalpartyofuganda.com")
    instagram = models.URLField(default="https://www.ecologicalpartyofuganda.com")
    linkedin = models.URLField(default="https://www.ecologicalpartyofuganda.com")
    is_external = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

class Candidate(models.Model):
    member = models.ForeignKey(Member, related_name="candidancies", on_delete=models.CASCADE)
    position = models.CharField(max_length=255, blank=False, default="")
    year = models.CharField(max_length=255, blank=False, default="")
    poster = models.ImageField(upload_to=get_upload_path, blank=True)
    elected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.position}-{self.year}"

class Blog(models.Model):
    author = models.ForeignKey(Member, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, default="")
    slug = models.SlugField(max_length=255, blank=True, default="")
    category = models.CharField(max_length=255, blank=False, default="")
    content = RichTextUploadingField(null=False, blank=False)
    thumbnail = models.ImageField(upload_to=f'news/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)
    authored_at = models.DateTimeField(blank=False)
    source = models.URLField(default=get_absolute_url_default)
    source_name = models.CharField(max_length=255, blank=False, default="EPU")

    class Meta:
        ordering = ('created_at',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        date_str = self.updated_at.strftime('%Y/%m/%d')
        year = int(date_str.split('/')[0])
        month = int(date_str.split('/')[1])
        day = int(date_str.split('/')[2])
        return reverse('main:blog_details', args=[year, month, day, self.slug, self.id])