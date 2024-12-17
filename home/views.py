from django.shortcuts import render, redirect
from .models import Categoria, Cliente
from django.contrib import messages
from .forms import CategoriaForm, ClienteForm

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
    except Categoria.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            # Reorganizar as ordens para manter consistência
            categorias = Categoria.objects.all().order_by('ordem')
            for index, cat in enumerate(categorias, start=1):
                cat.ordem = index
                cat.save()
            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('lista')
    else: 
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria/formulario.html', {'form': form})

def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()

    # Reorganizar os valores do campo 'ordem'
    categorias = Categoria.objects.all().order_by('ordem')
    for index, cat in enumerate(categorias, start=1):
        cat.ordem = index
        cat.save()

    messages.success(request, 'Categoria deletada e ordem atualizada com sucesso!')
    return redirect('lista')

def detalhe_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)
    contexto = {
        'form': form,
    }
    return render(request, 'categoria/detail.html', contexto)

def form_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('form_cliente')
    else:
        form = ClienteForm()
    
    # Obter todos os clientes
    clientes = Cliente.objects.all()
    return render(request, 'categoria/cliente.html', {'form': form, 'clientes': clientes})