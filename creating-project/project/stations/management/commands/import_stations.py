import csv

from django.core.management.base import BaseCommand
from stations.models import Station, Route


class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_filename = 'moscow_bus_stations.csv'
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                latitude = row['Latitude_WGS84']
                longitude = row['Longitude_WGS84']
                name = row['Name']
                station = Station.objects.create(
                    latitude=latitude,
                    longitude=longitude,
                    name=name
                )
                route_names = row['RouteNumbers'].split('; ')
                routes = [Route.objects.get_or_create(name=name)[0] for name in route_names]
                station.routes.set(routes)
