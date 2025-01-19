from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from django.apps import apps

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
# Clientes Formulário
def cliente(request):
    contexto={
        'listaCliente': Cliente.objects.all().order_by('-id')
    }
    return render(request,'cliente/lista.html', contexto)

def form_cliente(request):
    if (request.method == 'POST'):
        form = ClienteForm(request.POST)
        if form.is_valid():
            salvando = form.save()
            listaCliente=[]
            listaCliente.append(salvando)
            messages.success(request, 'Operação realizda com Sucesso.')
            return render(request, 'cliente/lista.html', {'listaCliente':listaCliente,})
        
    else: 
        form = ClienteForm()
    
    return render(request, 'cliente/formulario.html', {'form': form,})


def editar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')

    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            listaCliente=[]
            listaCliente.append(cliente)
            return render(request, 'cliente/lista.html', {'listaCliente':listaCliente,})

    else: 
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente/formulario.html', {'form':form,})


def remover_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        messages.success(request, 'Exclusão realizda com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')
    
    return redirect('listaCliente')

def detalhe_cliente(request, id):
    try:
        cliente = get_object_or_404(Cliente, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaCliente')

    return render(request, 'cliente/detalhes.html', {'cliente':cliente,})
def produto(request):
    contexto={
        'listaProduto': Produto.objects.all().order_by('-id')
    }
    return render(request,'produto/lista.html', contexto)

def form_produto(request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            salvando = form.save()
            listaProduto=[]
            listaProduto.append(salvando)
            messages.success(request, 'Operação realizda com Sucesso.')
            return render(request, 'produto/lista.html', {'listaProduto':listaProduto,})
        
    else: 
        form = ProdutoForm()
    
    return render(request, 'produto/formulario.html', {'form': form,})


def editar_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')

    if (request.method == 'POST'):
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save()
            listaProduto=[]
            listaProduto.append(produto)
           
            return redirect('listaProduto')

    else: 
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produto/formulario.html', {'form':form,})

def remover_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
        produto.delete()
        messages.success(request, 'Exclusão realizda com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')
    
    return redirect('listaProduto')

def detalhe_produto(request, id):
    try:
        produto = get_object_or_404(Produto, pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('listaProduto')

    return render(request, 'produto/detalhes.html', {'produto':produto,})



def ajustar_estoque(request, id):
    produto = Produto.objects.get(pk=id)
    estoque = produto.estoque 
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            estoque = form.save()
            listaProduto = []
            listaProduto.append(estoque.produto) 
            return redirect('listaProduto')
            # return render(request, 'produto/lista.html', {'listaProduto': listaProduto})
    else:
         form = EstoqueForm(instance=estoque)
    return render(request, 'produto/estoque.html', {'form': form,})


def teste1(request):
    return render(request, 'testes/teste1.html')

def teste2(request):
    return render(request, 'testes/teste2.html')

def buscar_dados(request, app_modelo):
    termo = request.GET.get('q', '') 
    try:
        
        app, modelo = app_modelo.split('.')
        modelo = apps.get_model(app, modelo)
    except LookupError:
        return JsonResponse({'error': 'Modelo não encontrado'}, status=404)
    
   
    if not hasattr(modelo, 'nome') or not hasattr(modelo, 'id'):
        return JsonResponse({'error': 'Modelo deve ter campos "id" e "nome"'}, status=400)
    
    resultados = modelo.objects.filter(nome__icontains=termo)
    dados = [{'id': obj.id, 'nome': obj.nome} for obj in resultados]
    return JsonResponse(dados, safe=False)

def teste3(request):
    return render(request, 'testes/teste3.html')