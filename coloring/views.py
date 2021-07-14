from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def interaction(request):
    return render(request, 'coloring/new_interaction.html')