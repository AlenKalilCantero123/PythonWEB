# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página de inicio usa PostListView
    path('', views.PostListView.as_view(), name='home'),

    # Página "Acerca de mí"
    path('about/', views.about, name='about'),

    # Página de publicaciones (corregido el nombre de la ruta)
    path('pages/', views.pages, name='pages'),

    # Crear publicación (usa la vista basada en clase PostCreateView)
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),

    # Buscar publicaciones
    path('search/', views.search_posts, name='search_posts'),

    # Ruta para ver el detalle de un post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Ruta para borrar un post (confirmación de borrado)
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Redirección después de logout
    # Esta ruta se elimina si usas LOGOUT_REDIRECT_URL en settings.py
    # path('logout_redirect/', views.logout_redirect, name='logout_redirect'),

    # Registro de usuario
    path('signup/', views.signup, name='signup'),

    # Perfil de usuario
    path('profile/', views.profile, name='profile'),
]
