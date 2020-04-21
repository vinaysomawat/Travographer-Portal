from django.shortcuts import render

# Create your views here.

def imagelist(request):
    return render(request, 'imagelist.html', {})
