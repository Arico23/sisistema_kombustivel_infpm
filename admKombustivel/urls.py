from django.urls import path
from . import views
urlpatterns = [
     path('', views.dash_kombustivel, name='dash_kombustivel'),
     # path('dadus_kom/', views.dadus_kom, name='dadus_kom'),
     path('aumenta_distributor/', views.aumenta_distributor, name='aumenta_distributor'),
     path('dadus_distributor/', views.dadus_distributor, name='dadus_distributor'),
     path('distribui_kom/', views.distribui_kom, name='distribui_kom'),
     # path('aumenta_dadus_kom/', views.aumenta_dadus_kom, name='aumenta_dadus_kom'),
     # path('deleteKombustivel/<str:pk>/', views.deleteKombustivel, name='apagaDadus'),
     # path('update_kom/<str:pk>/', views.updateKombustivel, name='updateKombustivel'),
     path('aumenta_dadus_distribuisaun/', views.aumenta_dadus_distribuisaun, name='aumenta_dadus_distribuisaun'),
     path('dadus_trans/', views.dadus_trans, name='dadus_trans'),
     path('aumenta_dadus_trans/', views.aumenta_dadus_trans, name='aumenta_dadus_transporte'),
     path('delete_dadus_trans/<str:pk>/', views.delete_dadus_transporte, name='delete_dadus_transporte'),
     path('updatetransporte/<str:pk>/', views.updateTransporte, name='updateTransporte'),
     path('dadus_motorista/', views.dadus_motorista, name='dadus_motorista'),
     path('aumenta_dadus_motorista/', views.aumenta_dadus_motorista, name='aumenta_dadus_motorista'),
     path('delete_dadus_motorista/<str:pk>/', views.delete_dadus_motorista, name='delete_dadus_motorista'),
     path('update_motorista/<str:pk>/', views.updateMotorista, name='updateMotorista'),
     path('aumenta_admin/', views.aumenta_admin, name='aumenta_admin'),  
     path('edit_admin/', views.edit_admin, name='edit_admin'),

]