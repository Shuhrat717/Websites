from django.shortcuts import render
from .models import Team, Company, History
from apps.cars.models import Cars
from apps.blog.models import Blog
from .forms import TripForm
from django.db.models import Q


def index(request):
    cars = Cars.objects.all().order_by('-id')
    posts = Blog.objects.all().order_by('-id')
    teams = Team.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        form = TripForm(request.POST)

        sd = request.POST.get('sd')
        ed = request.POST.get('ed')
        free_cars = Cars.objects.filter(
            ~Q(trips__journey_date__range=[sd, ed]) or ~Q(trips__return_date__range=[sd, ed]))

    context = {
        'cars': cars,
        'posts': posts,
        'teams': teams

    }

    return render(request, 'index.html', context)


def about(request):
    teams = Team.objects.all().order_by('-id')
    companies = Company.objects.all()
    histories = History.objects.all()
    context = {
        'teams': teams,
        'companies': companies,
        'histories': histories
    }

    return render(request, 'about.html', context)

