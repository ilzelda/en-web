from django.shortcuts import render, redirect
from .forms import PlanetModelForm

# Create your views here.
def showUniverse(request):
    return render(request, 'universe.html')


def createPlanet(request):
    if request.method == "POST":
        form = PlanetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('universe')
    else :
        form = PlanetModelForm()
        return render(request, 'new_planet.html', {'form':form})    

    