from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import Image


class Home(TemplateView):
    TemplateView = 'home.html'



def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        upload = Image(Imagefile=uploaded_file)
        upload.save()
        image_url = upload.Imagefile.url
    return render(request, 'upload.html', {
        'image_url':image_url
    })

    return render(request, 'upload.html')

def image_list(request):
    images = Image.objects.all()
    return render(request, 'upload.html', {
        'images': images
    })