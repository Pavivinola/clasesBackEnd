from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('inicio', views.inicio, name = 'inicio'),
    path('market', views.market, name= 'market'),
    path('market/crear', views.crear, name='crear'),
    path('eliminar/<int:producto_id>/', views.eliminar, name='eliminar')
    
]
