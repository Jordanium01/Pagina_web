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
from .forms import SignUpForm, ExtraInformation
from .models import UserExtraInfo

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
		return render(request, 'usuario/login.html')

	pass_valido = check_password(v_password, obj_user.password)

	if not pass_valido:
		return render(request, 'usuario/login.html')
	
	Token.objects.get_or_create(user=obj_user)
	login(request, obj_user)
	return redirect('index')
	
def logout_api(request):
    logout(request)
    return redirect('index')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        extra = ExtraInformation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            #Registrar los datos extra del usuario
            suscribe_box = extra['is_suscribe'].value()
            direccion_input = extra['direccion'].value()

            print(suscribe_box)
            UserExtraInfo.objects.create(id_id=request.user.id,is_suscribe=suscribe_box, direccion=direccion_input)

            return redirect('index')
    else:
        form = SignUpForm()
        extra = ExtraInformation()
    return render(request, 'usuario/registro.html', {'form_pag': form,'extra_pag': extra})