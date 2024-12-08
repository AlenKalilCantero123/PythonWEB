from django.db import models

# Modelo de Autor
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")  # Campo opcional para más información

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name

# Modelo de Categoría
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

# Modelo de Post
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Autor",
    )  # Relación con Author
    category = models.ManyToManyField(
        Category,
        related_name="posts",
        verbose_name="Categorías",
    )  # Relación ManyToMany con Category

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
