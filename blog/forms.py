from django import forms
from .models import Author, Category, Post


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']  # Asegúrate de que los campos existan en tu modelo

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']  # Asegúrate de que los campos existan en tu modelo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']  # Elimina 'author'
