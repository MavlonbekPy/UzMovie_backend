from django.contrib import admin
from .models import Genre, Actor, Director, Movie, Comment, Saved, Transaction


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'imdb_rating')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'is_active')


class SavedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'transaction_date')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Saved, SavedAdmin)
admin.site.register(Transaction, TransactionAdmin)
