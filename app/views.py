from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    img=Image.objects.all()
    return render(request,'home.html',{'img':img})

def contact(request):
    return render(request,'contact.html')

def contact_data(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if Contact.objects.filter(Email=email).exists():
            messages.error(request,'Email is already Exixts')
            return render(request,'contact.html')
        else:
            data=Contact.objects.create(Name=name,Email=email,Subject=subject,Message=message)
            data.save()
            return render(request,'home.html')
    else:
        return render(request,'contact.html')
    