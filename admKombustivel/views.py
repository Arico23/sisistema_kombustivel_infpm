from django.shortcuts import render
from .forms import DistribuisaunForm, TransporteForm, DistributorForm, MotoristaForm
from .models import *
from django.shortcuts import render, redirect


def dash_kombustivel (request):
    return render(request, 'templateKombustivel/dash_kombustivel.html')

#views Distribuitor 
def dadus_distributor (request):
    dadus_distributor = Distribuitor.objects.all()
    context = {'kombustivels': dadus_distributor}
    return render(request, 'templateKombustivel/distributor/dadus_distributor.html', context)

def aumenta_distributor (request):
    form = DistributorForm
    if request.method == 'POST':
        form = DistributorForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_distributor')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/distributor/aumenta_distributor.html', context)

#views stock kombustivel
# def dadus_kom (request):
#     dadus_kombustivel = Kombustivel.objects.all()
#     context = {'kombustivels': dadus_kombustivel}
#     return render(request, 'templateKombustivel/kombustivel/dadus_kom.html', context)

# def aumenta_dadus_kom (request):
#     form = KombustivelForm
#     if request.method == 'POST':
#         form = KombustivelForm(request.POST)
#         if form.is_valid():
#            form.save()
#            return redirect('dadus_kom')
         
#     context = {'form': form}
#     return render(request, 'templateKombustivel/kombustivel/aumenta_dadus_kom.html', context)

#views distribuisaun kombustivel
def distribui_kom (request):
    dadus_distribuisaun = Distribuisaun.objects.all()
    context = {'distribuisaun': dadus_distribuisaun}
    return render(request, 'templateKombustivel/kombustivel/distribui_kom.html', context)


def aumenta_dadus_distribuisaun (request):
    form = DistribuisaunForm
    if request.method == 'POST':
        form = DistribuisaunForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/distribui_kom')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/kombustivel/aumenta_dadus_distribuisaun.html', context)

# def deleteKombustivel(request, pk):
#     kombustivel = Kombustivel.objects.get(id_kombustivel=pk)
#     if request.method == 'GET':
#         kombustivel.delete()
#         return redirect('dadus_kom')

# def updateKombustivel (request, pk):
#     kombustivel = Kombustivel.objects.get(id_kombustivel=pk)
#     form = KombustivelForm(instance=kombustivel)
    
#     if request.method == 'POST':
#         # print('Printing Post', request.POST) print result form iha terminal
#         form = KombustivelForm(request.POST, instance=kombustivel)
#         if form.is_valid():
#             form.save()
#             return redirect('dadus_kom')
#     context = {'form': form}
#     return render(request, 'templateKombustivel/kombustivel/update_kom.html', context)

def dadus_trans (request):
    dadus_transporte = Transporte.objects.all()
    context = {'transporte': dadus_transporte}
    return render(request, 'templateKombustivel/transporte/dadus_trans.html', context)

def aumenta_dadus_trans (request):
    form = TransporteForm
    if request.method == 'POST':
        form = TransporteForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_trans')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/transporte/aumenta_dadus_trans.html', context)

def delete_dadus_transporte (request, pk):
    transporte = Transporte.objects.get(id_transporte=pk)
    if request.method == 'GET':
        transporte.delete()
        return redirect('dadus_trans')
 
def updateTransporte (request, pk):
    transporte = Transporte.objects.get(id_transporte=pk)
    form = TransporteForm(instance=transporte)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = TransporteForm(request.POST, instance=transporte)
        if form.is_valid():
            form.save()
            return redirect('dadus_trans')
    context = {'form': form}
    return render(request, 'templateKombustivel/transporte/edit_trans.html', context)

#Views dadus motorista
def dadus_motorista (request):
    dadus_motorista = Motorista.objects.all()
    context = {'motorista': dadus_motorista}
    return render(request, 'templateKombustivel/motorista/dadus_motorista.html', context)

def aumenta_dadus_motorista (request):
    form = MotoristaForm
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_motorista')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/motorista/aumenta_dadus_motorista.html', context)

def delete_dadus_motorista (request, pk):
    motorista = Motorista.objects.get(id_motorista=pk)
    if request.method == 'GET':
        motorista.delete()
        return redirect('dadus_motorista')
    
def updateMotorista (request, pk):
    motorista = Motorista.objects.get(id_motorista=pk)
    form = MotoristaForm(instance=motorista)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            return redirect('dadus_motorista')
    context = {'form': form}
    return render(request, 'templateKombustivel/motorista/update_motorista.html', context)

 


def index_admin (request):
        return render(request, 'templateKombustivel/admin/index_admin.html')


def aumenta_admin (request):
        return render(request, 'templateKombustivel/admin/aumenta_admin.html')

def edit_admin (request):
        return render(request, 'templateKombustivel/admin/edit_admin.html')

