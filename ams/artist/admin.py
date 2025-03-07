from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin

from artist.models import Artist


class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist


class ArtistAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ArtistResource


# Register your models here.
admin.site.register(Artist)
