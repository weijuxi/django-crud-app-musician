from django.shortcuts import redirect, render
from .models import Musician
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MusicForm
# Create your views here.

class MusicianCreate(CreateView):
    model = Musician
    fields = '__all__'
    success_url = '/musicians/'
    
class MusicianUpdate(UpdateView):
    model = Musician
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'age']

class MusicianDelete(DeleteView):
    model = Musician
    success_url = '/musicians/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def musicians_index(request):
    #search psql all cats
    musician = Musician.objects.all()
    return render(request, 'musicians/index.html', {'musicians': musician})


def musicians_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    music_form = MusicForm()
    return render(request, 'musicians/detail.html', {'musician': musician, 'music_form': music_form})

def add_music(request, musician_id):
    form = MusicForm(request.POST)
    if form.is_valid():
        new_music = form.save(commit=False)
        new_music.musician_id =  musician_id
        new_music.save()
    return redirect('musician-detail', musician_id = musician_id)