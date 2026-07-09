from django.urls import path
from . import views
#URLS DES PROJETS

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projet/creer/', views.projet_create, name='projet_create'),
    path('projet/<int:id>/', views.projet_detail, name='projet_detail'),
    path('projet/<int:id>/modifier/', views.projet_update, name='projet_update'),
    path('projet/<int:id>/supprimer/', views.projet_delete, name='projet_delete'),

#URL DES TACHES 

     path('tache/creer/', views.tache_create, name='tache_create'),
     path('tache/<int:id>/', views.tache_detail, name='tache_detail'),
     path('tache/<int:id>/modifier/', views.tache_update, name='tache_update'),
     path('tache/<int:id>/supprimer/', views.tache_delete, name='tache_delete'),


 ]

 