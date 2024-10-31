from django.shortcuts import redirect, render
from .models import Musician, Tool
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import MusicForm
# Create your views here.

def associate_tool(request, musician_id, tool_id):
    # Note that you can pass a toy's id instead of the whole object
    Musician.objects.get(id=musician_id).tool.add(tool_id)
    return redirect('musician-detail', musician_id=musician_id)

def remove_tool(request, musician_id, tool_id):
    Musician.objects.get(id=musician_id).tool.remove(tool_id)
    return redirect('musician-detail', musician_id=musician_id)


class ToolCreate(CreateView):
    model = Tool
    fields = '__all__'
    success_url = '/tools/'

class ToolDetail(DetailView):
    model = Tool
    
class ToolList(ListView):
    model = Tool
    
class ToolUpdate(UpdateView):
    model = Tool
    fields = ['name']
    
class ToolDelete(DeleteView):
    model = Tool
    success_url = '/tools/'
    
    
class MusicianCreate(CreateView):
    model = Musician
    fields = ['name', 'description', 'age']
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
    tools = Tool.objects.exclude(id__in = musician.tool.all().values_list('id'))
    music_form = MusicForm()
    return render(request, 'musicians/detail.html', {'musician': musician, 'music_form': music_form, 'tools': tools})

def add_music(request, musician_id):
    form = MusicForm(request.POST)
    if form.is_valid():
        new_music = form.save(commit=False)
        new_music.musician_id =  musician_id
        new_music.save()
    return redirect('musician-detail', musician_id = musician_id)