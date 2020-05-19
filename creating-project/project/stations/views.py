from django.shortcuts import render, get_object_or_404
from .models import Route, Station


def stations_view(request):
    routes = Route.objects.all()
    route_name = request.GET.get('route')
    if route_name:
        route = get_object_or_404(Route, name=route_name)
        stations = route.stations.all()
        first = stations.first()
        last = stations.last()
        center = {
            'x': (first.latitude + last.latitude) // 2,
            'y': (first.longitude + last.longitude) // 2
        }

        return render(
            request,
            'stations.html',
            context={
                'routes': routes,
                'route': route,
                'stations': stations,
                'center': center,
            }
        )
    return render(
        request,
        'stations.html',
        context={'routes': routes}
    )
