from django.shortcuts import render
from .forms import DistribuisaunForm, TransporteForm, DistributorForm, MotoristaForm, SenhasForm, RegionalForm, DepartamentuForm, DiresaunForm, FulanForm, TinanForm
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('dash_kombustivel')
        else:
            messages.info(request, 'Username or Password is incorrect')
                
        
    context = {}
        
    return render(request, 'templateKombustivel/Login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dash_kombustivel (request):
    return render(request, 'templateKombustivel/dash_kombustivel.html')

#views Distribuitor 
@login_required(login_url='login')
def dadus_distributor (request):
    dadus_distributor = Distribuitor.objects.all()
    context = {'kombustivels': dadus_distributor}
    return render(request, 'templateKombustivel/distributor/dadus_distributor.html', context)

@login_required(login_url='login')
def aumenta_distributor (request):
    form = DistributorForm
    if request.method == 'POST':
        form = DistributorForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_distributor')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/distributor/aumenta_distributor.html', context)

@login_required(login_url='login')
def delete_dadus_distributor (request, pk):
    distributor = Distribuitor.objects.get(id_distribuitor=pk)
    if request.method == 'GET':
        distributor.delete()
        return redirect('dadus_distributor')

@login_required(login_url='login')
def updateDistributor (request, pk):
    distributor = Distribuitor.objects.get(id_distribuitor=pk)
    form = DistributorForm(instance=distributor)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = DistributorForm(request.POST, instance=distributor)
        if form.is_valid():
            form.save()
            return redirect('dadus_distributor')
    context = {'form': form}
    return render(request, 'templateKombustivel/distributor/update_dadus_distributor.html', context)

    

#views distribuisaun kombustivel
@login_required(login_url='login')
def distribui_kom (request):
    dadus_distribuisaun = Distribuisaun.objects.all()
    context = {'distribuisaun': dadus_distribuisaun}
    return render(request, 'templateKombustivel/kombustivel/distribui_kom.html', context)


@login_required(login_url='login')
def aumenta_dadus_distribuisaun (request):
    form = DistribuisaunForm
    if request.method == 'POST':
        form = DistribuisaunForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/distribui_kom')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/kombustivel/aumenta_dadus_distribuisaun.html', context)

#views senhas
@login_required(login_url='login')
def senhas (request):
    dadus_senhas = Senhas.objects.all()
    context = {'kombustivels': dadus_senhas}
    return render(request, 'templateKombustivel/senhas/senhas.html', context)

@login_required(login_url='login')
def aumenta_dadus_senhas (request):
    form = SenhasForm
    if request.method == 'POST':
        form = SenhasForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_senhas')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/senhas/aumenta_dadus_senhas.html', context)

@login_required(login_url='login')
def delete_dadus_senhas (request, pk):
    senhas = Senhas.objects.get(id_senhas=pk)
    if request.method == 'GET':
        senhas.delete()
        return redirect('dadus_senhas')
  
@login_required(login_url='login')  
def updateSenhas (request, pk):
    senhas = Senhas.objects.get(id_senhas=pk)
    form = SenhasForm(instance=senhas)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = SenhasForm(request.POST, instance=senhas)
        if form.is_valid():
            form.save()
            return redirect('dadus_senhas')
    context = {'form': form}
    return render(request, 'templateKombustivel/senhas/update_senhas.html', context)

#views regionsal
@login_required(login_url='login')
def dadus_regional (request):
    dadus_regional = Regional.objects.all()
    context = {'kombustivels': dadus_regional}
    return render(request, 'templateKombustivel/regional/dadus_regional.html', context)

@login_required(login_url='login')
def aumenta_dadus_regional (request):
    form = RegionalForm
    if request.method == 'POST':
        form = RegionalForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_regional')
        
    context = {'form': form}
    return render(request, 'templateKombustivel/regional/aumenta_dadus_regional.html', context)

@login_required(login_url='login')
def delete_dadus_regional (request, pk):
    regional = Regional.objects.get(id_regional=pk)
    if request.method == 'GET':
        regional.delete()
        return redirect('dadus_regional')

@login_required(login_url='login')
def updateRegional (request, pk):
    regional = Regional.objects.get(id_regional=pk)
    form = RegionalForm(instance=regional)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = RegionalForm(request.POST, instance=regional)
        if form.is_valid():
            form.save()
            return redirect('dadus_regional')
    context = {'form': form}
    return render(request, 'templateKombustivel/regional/update_regional.html', context)

#views departamentu
@login_required(login_url='login')
def dadus_departamentu (request):
    dadus_departamentu = Departamentu.objects.all()
    context = {'kombustivels': dadus_departamentu}
    return render(request, 'templateKombustivel/departamentu/dadus_departamentu.html', context)

@login_required(login_url='login')
def aumenta_dadus_departamentu (request):
    form = DepartamentuForm
    if request.method == 'POST':
        form = DepartamentuForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_departamentu')
        
    context = {'form': form}
    return render(request, 'templateKombustivel/departamentu/aumenta_dadus_departamentu.html', context)

@login_required(login_url='login')
def delete_dadus_departamentu (request, pk):
    departamentu = Departamentu.objects.get(id_departamentu=pk)
    if request.method == 'GET':
        departamentu.delete()
        return redirect('dadus_departamentu')

@login_required(login_url='login')
def updateDepartamentu (request, pk):
    departamentu = Departamentu.objects.get(id_departamentu=pk)
    form = DepartamentuForm(instance=departamentu)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = DepartamentuForm(request.POST, instance=departamentu)
        if form.is_valid():
            form.save()
            return redirect('dadus_departamentu')
    context = {'form': form}
    return render(request, 'templateKombustivel/departamentu/update_departamentu.html', context)

@login_required(login_url='login')
def dadus_diresaun (request):
    dadus_diresaun = Diresaun.objects.all()
    context = {'kombustivels': dadus_diresaun}
    return render(request, 'templateKombustivel/diresaun/dadus_diresaun.html', context)

@login_required(login_url='login')
def aumenta_dadus_diresaun (request):
    form = DiresaunForm
    if request.method == 'POST':
        form = DiresaunForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_diresaun')
        
    context = {'form': form}
    return render(request, 'templateKombustivel/diresaun/aumenta_dadus_diresaun.html', context)


@login_required(login_url='login')
def delete_dadus_diresaun (request, pk):
    diresaun = Diresaun.objects.get(id_diresaun=pk)
    if request.method == 'GET':
        diresaun.delete()
        return redirect('dadus_diresaun')

@login_required(login_url='login')    
def updateDiresaun (request, pk):
    diresaun = Diresaun.objects.get(id_diresaun=pk)
    form = DiresaunForm(instance=diresaun)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = DiresaunForm(request.POST, instance=diresaun)
        if form.is_valid():
            form.save()
            return redirect('dadus_diresaun')
    context = {'form': form}
    return render(request, 'templateKombustivel/diresaun/update_diresaun.html', context)

#views fulan
@login_required(login_url='login')
def dadus_fulan (request):
    dadus_fulan = Fulan.objects.all()
    context = {'kombustivels': dadus_fulan}
    return render(request, 'templateKombustivel/fulan/dadus_fulan.html', context)

@login_required(login_url='login')
def aumenta_dadus_fulan (request):
    form = FulanForm
    if request.method == 'POST':
        form = FulanForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_fulan')
        
    context = {'form': form}
    return render(request, 'templateKombustivel/fulan/aumenta_dadus_fulan.html', context)


@login_required(login_url='login')
def delete_dadus_fulan (request, pk):
    fulan = Fulan.objects.get(id_fulan=pk)
    if request.method == 'GET':
        fulan.delete()
        return redirect('dadus_fulan')

@login_required(login_url='login')    
def updateFulan (request, pk):
    fulan = Fulan.objects.get(id_fulan=pk)
    form = FulanForm(instance=fulan)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = FulanForm(request.POST, instance=fulan)
        if form.is_valid():
            form.save()
            return redirect('dadus_fulan')
    context = {'form': form}
    return render(request, 'templateKombustivel/fulan/update_fulan.html', context)

#views fulan
@login_required(login_url='login')
def dadus_tinan (request):
    dadus_tinan = Tinan.objects.all()
    context = {'kombustivels': dadus_tinan}
    return render(request, 'templateKombustivel/tinan/dadus_tinan.html', context)

@login_required(login_url='login')
def aumenta_dadus_tinan (request):
    form = TinanForm
    if request.method == 'POST':
        form = TinanForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_tinan')
    context = {'form': form}
    return render(request, 'templateKombustivel/tinan/aumenta_dadus_tinan.html', context)

@login_required(login_url='login')
def delete_dadus_tinan (request, pk):
    tinan = Tinan.objects.get(ano=pk)
    if request.method == 'GET':
        tinan.delete()
        return redirect('dadus_tinan')
 
@login_required(login_url='login')   
def updateTinan (request, pk):
    tinan = Tinan.objects.get(ano=pk)
    form = TinanForm(instance=tinan)
    
    if request.method == 'POST':
        # print('Printing Post', request.POST) print result form iha terminal
        form = TinanForm(request.POST, instance=tinan)
        if form.is_valid():
            form.save()
            return redirect('dadus_tinan')
    context = {'form': form}
    return render(request, 'templateKombustivel/tinan/update_tinan.html', context)

@login_required(login_url='login')
def dadus_trans (request):
    dadus_transporte = Transporte.objects.all()
    context = {'transporte': dadus_transporte}
    return render(request, 'templateKombustivel/transporte/dadus_trans.html', context)

@login_required(login_url='login')
def aumenta_dadus_trans (request):
    form = TransporteForm
    if request.method == 'POST':
        form = TransporteForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_trans')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/transporte/aumenta_dadus_trans.html', context)

@login_required(login_url='login')
def delete_dadus_transporte (request, pk):
    transporte = Transporte.objects.get(id_transporte=pk)
    if request.method == 'GET':
        transporte.delete()
        return redirect('dadus_trans')
 
@login_required(login_url='login')
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
@login_required(login_url='login')
def dadus_motorista (request):
    dadus_motorista = Motorista.objects.all()
    context = {'motorista': dadus_motorista}
    return render(request, 'templateKombustivel/motorista/dadus_motorista.html', context)

@login_required(login_url='login')
def aumenta_dadus_motorista (request):
    form = MotoristaForm
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dadus_motorista')
         
    context = {'form': form}
    return render(request, 'templateKombustivel/motorista/aumenta_dadus_motorista.html', context)

@login_required(login_url='login')
def delete_dadus_motorista (request, pk):
    motorista = Motorista.objects.get(id_motorista=pk)
    if request.method == 'GET':
        motorista.delete()
        return redirect('dadus_motorista')

@login_required(login_url='login')    
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

@login_required(login_url='login')
def stockIn (request):
    stockIn = Distribuitor.objects.all()
    context = {'kombustivels': stockIn}
    return render(request, 'templateKombustivel/relatorio/stockIn.html', context)

@login_required(login_url='login')
def index_admin (request):
        return render(request, 'templateKombustivel/admin/index_admin.html')

@login_required(login_url='login')
def aumenta_admin (request):
        return render(request, 'templateKombustivel/admin/aumenta_admin.html')

@login_required(login_url='login')
def edit_admin (request):
        return render(request, 'templateKombustivel/admin/edit_admin.html')

