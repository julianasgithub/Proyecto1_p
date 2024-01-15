'''from django.shortcuts import render, redirect, get_object_or_404
from equipamiento.models import Post
from equipamiento.models import Categoria
# Create your views here.

def equipamiento(request):
    posts=Post.objects.all()
    return render (request, "equipamiento/equipamiento.html", {"posts":posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, 'equipamiento/categoria.html', {'categoria':categoria, "posts":posts})
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def cargar_archivo(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.archivo = form.cleaned_data['archivo']
            post.save()
    else:
        form = PostForm(instance=post)

    return render(request, 'cargar_archivo.html', {'form': form, 'post': post})

'''