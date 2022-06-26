from django.shortcuts import render
from django.views import View
from .models import Place, Sport, Food, Type, District
from django.http import HttpRequest, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import models


# Create your views here.
class MainPage(View):
    def get(self, request):
        return render(request, "main_page.html")

#widok dla zalogowanego użytkownika, create superuser, jest model w Django użytkownika
#usunąć migrations i zrobić jeszcze makemigrations
#widok dla każdej dany wyszukanej
#dodać z 2 miejsca
#nad widokami dodać dokumentacje
#jeden test
#usunąć sqlite
#na nowo zrobić bazę danych


@csrf_exempt
def formpage(request):
    if request.method == 'POST':
        html = "<html><body>Miejsce dodane</body></html>"
        place = Place()
        district = District()
        type = Type()
        food = Food()
        sport = Sport()
        place.name = request.POST.get('name')
        place.address = request.POST.get('address')
        district.name = request.POST.get('district')
        type.cat = request.POST.get('type')
        food.cuisine = request.POST.get('cuisine')
        sport.kind = request.POST.get('sport')
        place.save()
        district.save()
        type.save()
        food.save()
        sport.save()
        return HttpResponse(html)
    else:
        return render(request, 'form.html')

