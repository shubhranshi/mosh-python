from django.contrib import admin
from .models import Genre, Movie        # We use the "." to indicate the current folder.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # fields = ('title', 'genre')
    exclude = ('date_created', ) # need to include ','
    list_display = ('title', 'number_in_stock', 'daily_rate')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

