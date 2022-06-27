from django.shortcuts import render
from django.views import View
from .models import Place, Sport, Food, Type, District
from django.http import HttpRequest, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .forms import LoginForm

#class MainPage - gives form which after filling in redirects us to view "view" in which we have informations from models.
#View user_login allows you to log in to get option "Dodaj miejsce" in view formpage, which adds data to models.
#User for option user_login(login: 'darth.vader', password:'padme')

# Create your views here.
class MainPage(View):
    def get(self, request):
        district = District.objects.all()
        type = Type.objects.all()
        food = Food.objects.all()
        sport = Sport.objects.all()
        context = {
            "district": district,
            "type": type,
            "food": food,
            "sport": sport
        }
        return render(request, "main_page.html", context)









def view(request):
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
    context = {
        "places": place,
        "types": type,
        "foods": food,
        "sports": sport
    }
    if place.name and type.cat:
        return render(request, "data.html", context)

def formpage(request):
    food_all = Food.objects.all()
    sport_all = Sport.objects.all()
    context = {
        "food": food_all,
        "sport": sport_all
    }
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
        return render(request, 'form.html', context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'login_view.html')
                else:
                    return HttpResponse('Zablokowany')
            else:
                form = LoginForm()
            return render(request, 'login.html', {'form': form})
