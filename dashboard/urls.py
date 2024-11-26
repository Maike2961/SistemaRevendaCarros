from django.urls import path
from .views import dashboard, editar, delete

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('editar/<uuid:id>/', editar, name='editar'),
    path('delete/<uuid:id>/', delete, name='delete')
]