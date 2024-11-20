from django.urls import path
from .views import dashboard, editar

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('editar/<uuid:id>/', editar, name='editar')
]