# blog/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm

# Vista de prueba para asegurarse de que el servidor esté funcionando
def index(request):
    return HttpResponse("Hello, World!")

# Página de inicio (home)
def home(request):
    return render(request, 'blog/home.html')

# Página "Acerca de mí"
def about(request):
    # Información del propietario para mostrar en la página "Acerca de mí"
    owner_info = {
        'name': 'Tu Nombre',
        'avatar_url': 'https://www.example.com/tu_avatar.jpg',  # Asegúrate de tener una URL válida para tu avatar
        'bio': 'Aquí va tu biografía.',
        'contact': 'tu_email@example.com'
    }
    return render(request, 'blog/about.html', {'owner_info': owner_info})

# Crear un autor
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige al home después de guardar el autor
    else:
        form = AuthorForm()

    model_name = Author._meta.model_name

    return render(request, 'blog/create_author.html', {'form': form, 'model_name': model_name})

# Crear una categoría
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige al home después de guardar la categoría
    else:
        form = CategoryForm()
    
    model_name = Category._meta.model_name

    return render(request, 'blog/create_category.html', {'form': form, 'model_name': model_name})

# Crear un post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige al home después de guardar el post
    else:
        form = PostForm()
    
    model_name = Post._meta.model_name

    return render(request, 'blog/create_post.html', {'form': form, 'model_name': model_name})

# Buscar posts
def search_posts(request):
    query = request.GET.get('q', '')  # Obtener el query de la URL
    results = Post.objects.filter(title__icontains=query) if query else []  # Consulta optimizada si no hay query

    return render(request, 'blog/search.html', {'query': query, 'results': results})
