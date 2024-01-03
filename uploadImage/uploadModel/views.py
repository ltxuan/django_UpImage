from django.shortcuts import render
from django.http import HttpResponse
from .models import UpForm
from .forms import UploadFileForm
# Create your views here.
def uploadFile(request):
    UF = UploadFileForm
    return render(request, 'uploadModel/fileUpload.html', {'UF': UF})

def getFile(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        instance = UpForm(image2=request.FILES["image1"])
        instance.save()
        return HttpResponse("save file success")