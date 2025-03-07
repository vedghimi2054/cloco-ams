import pandas as pd
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from artist.serializers import ArtistImportSerializer


class ImportArtistView(CreateAPIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES.get('file')

        if not csv_file.name.endswith('.csv'):
            return Response({'error': 'Invalid file format. Please upload a CSV file.'}, status=400)

        # Use pandas to read the CSV file
        df = pd.read_csv(csv_file)
        print("CSV Columns:", df.columns)
        required_columns = ['id', 'name', 'dob', 'gender', 'address', 'first_release_year', 'no_of_albums_released']
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            return Response({'error': f'Missing columns in CSV: {", ".join(missing_columns)}'}, status=400)

        # Handle datetime conversion for the 'dob' column
        if 'dob' in df.columns:
            df['dob'] = pd.to_datetime(df['dob'], errors='coerce')  # Invalid datetime will be NaT (Not a Time)

        # Handle numeric conversion for 'first_release_year' and 'no_of_albums_released'
        if 'first_release_year' in df.columns:
            df['first_release_year'] = pd.to_numeric(df['first_release_year'], errors='coerce')
        if 'no_of_albums_released' in df.columns:
            df['no_of_albums_released'] = pd.to_numeric(df['no_of_albums_released'], errors='coerce')

        # Handle missing values (if necessary) or invalid rows
        df.dropna(subset=['dob', 'first_release_year', 'no_of_albums_released'], inplace=True)

        # Validate gender field (assuming 0 or 1 are valid gender values)
        if not df['gender'].isin([1, 2,3]).all():
            return Response({'error': 'Invalid gender value in CSV.'}, status=400)

        # Prepare artist data for serialization
        for index, row in df.iterrows():
            artist_data = {
                "id": row.get('id'),
                'name': row.get('name'),
                'dob': row.get('dob'),
                'gender': row.get('gender'),
                'address': row.get('address'),
                'first_release_year': row.get('first_release_year'),
                'no_of_albums_released': row.get('no_of_albums_released')
            }

            serializer = ArtistImportSerializer(data=artist_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'error': f"Invalid data in row {index + 1}."}, status=400)

        return Response({'message': 'Artists imported successfully!'}, status=201)
