from django.urls import path, include
from .views import index, cadastro,logout
from django.contrib.auth import views
from .forms import LoginForm

urlpatterns = [
    path('login/',  views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
    path('', index, name='index')
]