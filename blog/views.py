from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm

def index(request):
    return HttpResponse("Hello, World!")

def home(request):
    return render(request, 'blog/home.html')

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    
    # Obtener el nombre del modelo de manera correcta
    model_name = Author._meta.model_name  # Usamos Author aquí directamente

    return render(request, 'blog/create_author.html', {'form': form, 'model_name': model_name})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    model_name = Category._meta.model_name  # Usamos Category aquí directamente
    return render(request, 'blog/create_category.html', {'form': form, 'model_name': model_name})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    model_name = Post._meta.model_name  # Usamos Post aquí directamente
    return render(request, 'blog/create_post.html', {'form': form, 'model_name': model_name})

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else Post.objects.none()
    return render(request, 'blog/search.html', {'query': query, 'results': results})
