from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render (request,'generator/home.html')
def aboutus(request):
    return render (request,'generator/aboutus.html')

def password(request):
    newpassword=""
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special_characters'):
        characters.extend(list('!@#$%^&*'))
    
    
    length=int(request.GET.get('length',12))
               
    for i in range(length):
               
        newpassword+=random.choice(characters)
    return render (request,'generator/password.html',{'password':newpassword})
