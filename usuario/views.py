from django.shortcuts import render

# Create your views here.

def login(request):
		return render(request,'usuario/login.html')

def regis(request):
		return render(request,'usuario/registro.html')
