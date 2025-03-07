from django.urls import path

from artist.views import SaveArtistView, UpdateArtistView, DeleteArtistView, GetAllArtistsView
from artist.views.csv_export import ExportArtistView
from artist.views.csv_import import ImportArtistView

urlpatterns = [
    # Artist end-point
    path("list", GetAllArtistsView.as_view(), name="get-all-artists"),
    path("create", SaveArtistView.as_view(), name="save-artist"),
    path("update/<int:pk>", UpdateArtistView.as_view(), name="update-artist"),
    path("delete/<int:pk>", DeleteArtistView.as_view(), name="delete-artist"),
    path("export", ExportArtistView.as_view(), name="export-artist"),
    path("import", ImportArtistView.as_view(), name="import-artist"),

]
