from django.shortcuts import render, redirect
from .models import Categoria
from django.contrib import messages
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
            messages.success(request, 'Operação cadastrada com sucesso!')
            return redirect('lista')
    else: 
        form = CategoriaForm()
    return render(request, 'categoria/formulario.html', {'form': form})


def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    if (request.method == 'POST'):
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save()
            lista=[]
            lista.append(categoria)
            return render(request, 'categoria/lista.html', {'lista':lista,})

    else: 
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria/formulario.html', {'form':form,})

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