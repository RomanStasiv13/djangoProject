from django.contrib import admin
from news.models import Author, Nation, Category, Tags, News

# Register your models here.
admin.site.register(Author)
admin.site.register(Nation)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(News)