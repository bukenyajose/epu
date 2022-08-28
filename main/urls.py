from django.urls import path

from . import views

app_name='main'
urlpatterns = [
    path('', views.home_view, name="home"),
    path('generate-sitemap', views.generate_sitemap, name='generate-sitemap'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:slug>/<int:id>', views.blog_details_view, name='blog_details'),
]
