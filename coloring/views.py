from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def interaction(request):
    return render(request, 'coloring/new_interaction.html')

def gallery(request):
    return render(request, 'coloring/gallery.html')

def interaction_trig(request):
    return render(request, 'coloring/new_interaction_trig.html')