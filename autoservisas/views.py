from django.shortcuts import render
from django.http import HttpResponse

from .models import Paslauga, Uzsakymas, Automobilis


def index(request):
 paslaugu_kiekis = Paslauga.objects.count()
 atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(status__exact='a').count()
 automobiliu_kiekis = Automobilis.objects.count()

 num_visits = request.session.get('num_visits', 1)
 request.session['num_visits'] = num_visits + 1

 context = {
  'paslaugu_kiekis': paslaugu_kiekis,
  'atliktu_uzsakymu_kiekis': atliktu_uzsakymu_kiekis,
  'automobiliu_kiekis': automobiliu_kiekis,
  'num_visits': num_visits,
 }

 return render(request, 'index.html', context=context)

