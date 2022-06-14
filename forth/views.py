from django.shortcuts import render

# Create your views here.

def list(request):
    context = {}

    return render(request, 'forth/list.html', context)