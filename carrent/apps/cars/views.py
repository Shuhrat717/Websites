from django.shortcuts import render
from .models import Cars
from apps.home.models import Trip
from django.db.models import Q


def cars(request):
    car = Cars.objects.all().order_by('-id')
    sd = request.POST.get('sd')
    ed = request.POST.get('ed')
    from_ = request.POST.get('from')
    to_ = request.POST.get('to')
    trips = Trip.objects.filter(Q(journey_date__range=[sd, ed]) or Q(return_date__range=[sd, ed]))
    for i in trips:
        car = car.exclude(id=i.car.id)
    print(from_)
    print(to_)
    print(sd)
    print(ed)
    context = {
        'cars': car,
        'sd': sd,
        'ed': ed,
        'from': from_,
        'to': to_,
    }
    return render(request, 'cars.html', context)


def success(request, pk=None):
    car = Cars.objects.get(id=pk)
    sd = request.GET.get('sd')
    ed = request.GET.get('ed')
    from_ = request.GET.get('from')
    to_ = request.GET.get('to')
    if request.method == 'POST':
        Trip.objects.create(
            car_id=pk,
            where_from=from_,
            where_go=to_,
            journey_date=sd,
            return_date=ed,
        )
        pass
    context = {
        'i': car,
    }
    return render(request, 'success.html', context)
