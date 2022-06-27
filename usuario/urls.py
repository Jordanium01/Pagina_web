from django.urls import path
from.views import regis
from .viewsLogin import login_api
urlpatterns = [
    path('login/', login_api, name="login"),
    #path('register/', regis, name="register")
]