# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('about/', views.about, name='about'),  # Página "Acerca de mí"
    path('create_author/', views.create_author, name='create_author'),  # Crear autor
    path('create_category/', views.create_category, name='create_category'),  # Crear categoría
    path('create_post/', views.create_post, name='create_post'),  # Crear publicación
    path('search/', views.search_posts, name='search_posts'),  # Buscar publicaciones
]
