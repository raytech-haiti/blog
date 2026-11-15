from django.contrib import admin
from post.models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','published', 'date_update', 'date_create')
    list_filter = ('published',)

admin.site.register(Articles, ArticlesAdmin)
