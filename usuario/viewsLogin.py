from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])#se ocupa un post por que el get muestra la informacion en el url
def login_api(request):
	data = JSONParser().parse(request)
	v_username = data['username']
	v_password = data['password']
	try:
		#obj lo declaro yo
		obj_user = User.objects.get(username = v_username)
	except User.DoesNotExist:
		return Response("Usuario invalido")
		
	v_pass_valido = check_password(v_password, obj_user.password)
	if not v_pass_valido:
		return Response("Password Incorrecta")
		
	token, created = Token.objects.get_or_create(user=obj_user)
	return Response(token.key)