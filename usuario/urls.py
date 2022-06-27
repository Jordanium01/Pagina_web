from django.urls import path, include
from.views import regis
from .viewsLogin import login_api, logout_api, signup

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login_api, name="sigin"),
    path('logout/', logout_api, name="sigout"),
    path('register/', signup, name="sigup"),
    
    #path('register/', regis, name="register")
    #google cosas
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

#978199114381-hfesqe28388jshsuu1ceen7699bta4u5.apps.googleusercontent.com
#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