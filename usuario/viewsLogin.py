from ast import parse
from urllib import request
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

#importar modelo
#from catalogos.models import Usuario

@api_view(['POST'])#se ocupa un post por que el get muestra la informacion en el url
def login_api(request):
	v_username = request.data['username']
	v_password = request.data['password']
	try:
		#obj lo declaro yo
		obj_user = User.objects.get(email = v_username)
	except User.DoesNotExist:
        #return Response("Usuario invalido" +  "/" + str(v_username))
		return render(request, 'usuario/login.html')

	pass_valido = check_password(v_password, obj_user.password)

	if not pass_valido:
        #return Response("Password incorrecta")
		return render(request, 'usuario/login.html')
	
	token, created = Token.objects.get_or_create(user=obj_user)
	login(request, obj_user)
	#return render(request,'catalogos/index.html') #Response(token.key)
	return redirect('index')
	
def logout_api(request):
    logout(request)
    return redirect('index')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'usuario/registro.html', {'form': form})