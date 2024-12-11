from django.shortcuts import render, redirect
from .models import Categoria
from .forms import CategoriaForm

def index(request):
    return render(request, 'index.html')

def categoria(request): 
    contexto = {
        'lista': Categoria.objects.all().order_by('-id'),
    }
    return render(request, 'categoria/lista.html', contexto)

def form_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else: 
        form = CategoriaForm()
    return render(request, 'categoria/formulario.html', {'form': form})

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else: 
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/formulario.html', {'form': form})

def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('lista')

def detalhe_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/detail.html', contexto)