from django.contrib import admin

from . import models

class CandidateInline(admin.TabularInline):
    model = models.Candidate

# Register your models here.
@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'role',
        'email',
    ]
    list_display_links = ("first_name",)
    list_filter = ("role",)
    search_fields = ("first_name", "last_name", "role",)
    inlines = (CandidateInline,)

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'author',
        'created_at',
        'updated_at',
    ]
    list_display_links = ("title",)
    list_filter = ("category", "author",)
    search_fields = ("category", "author", "title", "content",)