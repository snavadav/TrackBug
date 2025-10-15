from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('nuevo_ticket/', views.nuevo_ticket, name='nuevo_ticket'),
    path('perfil/', views.perfil, name='perfil'),
    path('tickets/<int:ticket_id>/', views.ver_ticket, name='ver_ticket'),
    path('logout/', views.logout_view, name='logout'),
]