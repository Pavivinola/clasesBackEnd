from django.urls import path
from . import views

urlpatterns = [ #esto sirve para definir las rutas de la app, se pasa de una vista a otra
    path('', views.inicio, name = 'inicio'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('inicio', views.inicio, name = 'inicio'),
    path('market', views.market, name= 'market'),
    path('market/crear', views.crear, name='crear'),
    path('eliminar/<int:producto_id>/', views.eliminar, name='eliminar'),
    path('prestar/<int:producto_id>/', views.prestar, name='prestar')
    
]
