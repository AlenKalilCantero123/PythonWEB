from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required  # Asegúrate de importar esto
from .models import Post
from .forms import PostForm

# Página "Acerca de mí"
def about(request):
    owner_info = {
        'name': 'Tu Nombre',
        'avatar_url': 'https://www.example.com/tu_avatar.jpg',
        'bio': 'Aquí va tu biografía.',
        'contact': 'tu_email@example.com'
    }
    return render(request, 'blog/about.html', {'owner_info': owner_info})

# Página "Pages"
def pages(request):
    return render(request, 'blog/pages.html')

# Vista de listado de publicaciones
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

# Vista de detalle de publicaciones
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Vista para crear un post (requiere login)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Asigna el autor al usuario autenticado
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')  # Redirige al home después de la creación

# Vista para editar un post (requiere login)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'

    def form_valid(self, form):
        # Verifica que el usuario sea el autor del post antes de permitir la edición
        if form.instance.author != self.request.user:
            return HttpResponseForbidden("No tienes permiso para editar este post.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

# Vista para borrar un post (requiere login)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')  # Redirige al home después de la eliminación

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        # Verifica que el post pertenezca al usuario que lo está eliminando
        if post.author != request.user:
            return HttpResponseForbidden("No tienes permiso para eliminar este post.")
        return super().delete(request, *args, **kwargs)

# Vista de perfil del usuario
@login_required
def profile(request):
    user = request.user
    return render(request, 'blog/profile.html', {'user': user})

# Vista de registro de usuarios
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Vista de búsqueda
def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'blog/search.html', {'query': query, 'results': results})

# Vista para borrar un post desde la página de inicio (requiere login)
@login_required
def delete_post_from_home(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Verifica que el post pertenezca al usuario que lo está eliminando
    if post.author == request.user:
        post.delete()
        return redirect('home')  # Redirige al home después de eliminar el post
    
    # Si el usuario no es el autor, muestra un error 403 (Forbidden)
    return HttpResponseForbidden("No tienes permiso para eliminar este post.")
