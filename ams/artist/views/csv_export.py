import csv

from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from artist.models import Artist
from artist.serializers import ArtistExportSerializer
from authentication.permission.artist import IsSuperAdminOrArtistManager


class ExportArtistView(ListAPIView):
    permission_classes = [IsSuperAdminOrArtistManager]
    queryset = Artist.objects.all()
    serializer_class = ArtistExportSerializer

    def get(self, request, *args, **kwargs):
        # Create the HttpResponse object with the appropriate CSV MIME type
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=artists.csv'

        # Create a CSV writer object
        writer = csv.writer(response)

        # Write the CSV header (column names)
        writer.writerow([field.name for field in Artist._meta.fields])

        # Write the data rows
        for artist in self.get_queryset():
            writer.writerow([getattr(artist, field.name) for field in Artist._meta.fields])

        return response
