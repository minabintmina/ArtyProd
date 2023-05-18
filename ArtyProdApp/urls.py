from django.urls import path,include
from . import views


urlpatterns = [
    path('projects', views.projects, name='Projects'),
    path('portfolio', views.portfolio, name='Portfolio'),
    path('services', views.service,name='Services'),
    path('personnel', views.personnel,name='Personnel'),
    path('signup', views.signup,name='SignUp'),
    path('login', views.login, name='Login'),
    path('contact', views.contact,name='Contact'),
    path('project', views.project, name='Project'),
    path('MyProjects', views.Myproject, name='myprojects')
]