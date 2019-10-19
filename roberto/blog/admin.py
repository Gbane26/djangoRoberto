# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'title',
        'statut',
        'date_add',
        'date_update',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
        'Category_id',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'Category_id',
        'id',
        'title',
        'description',
        'image',
        'statut',
        'date_add',
        'date_update',
        'Category_id',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'Category_id')
    list_filter = ('Category_id', 'id', 'Category_id')


class InstagramAdmin(admin.ModelAdmin):

    list_display = ('id', 'image', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'email',
        'statut',
        'date_add',
        'date_update',
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'author',
        'email',
        'message',
        'website',
        'date_add',
        'Article_id',
    )
    list_filter = (
        'date_add',
        'Article_id',
        'id',
        'author',
        'email',
        'message',
        'website',
        'date_add',
        'Article_id',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Tag, TagAdmin)
_register(models.Instagram, InstagramAdmin)
_register(models.Newsletter, NewsletterAdmin)
_register(models.Comment, CommentAdmin)
