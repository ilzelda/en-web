from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlanetModelForm, CommentModelForm
from .models import Planet

# Create your views here.
def showUniverse(request):
    planets = Planet.objects.all()
    form = CommentModelForm()
    return render(request, 'universe.html', {'planets':planets})


def createPlanet(request):
    if (request.method == "POST" or request.method == "FILES"):
        form = PlanetModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('universe')
    else :
        form = PlanetModelForm()
        return render(request, 'new_planet.html', {'form':form})    

def showPlanetDetail(request, planet_id):
    planet = get_object_or_404(Planet, pk=planet_id)
    form = CommentModelForm()
    return render(request, 'planet_detail.html', {'planet':planet, 'comment_form':form})


def createComment(request, planet_id):
    filled_form = CommentModelForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit = False)
        finished_form.planet = get_object_or_404(Planet, pk = planet_id)
        finished_form.save()
    
    return redirect('planetdetail', planet_id)