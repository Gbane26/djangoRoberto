from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'message',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'name',
        'email',
        'message',
        'statut',
        'date_add',
        'date_update',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
