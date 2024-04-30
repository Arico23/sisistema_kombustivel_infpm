from django.contrib import admin

from .models import *

class admKombustivelAdminUtilizador(admin.ModelAdmin):
    list_display = ('id_user','username', 'password', 'level')
    list_filter = ('username', 'password', 'level')
    search_fields = ('username', 'password', 'level')

#registu model ba admin django
admin.site.register(Utilizador, admKombustivelAdminUtilizador)


class admKombustivelAdminTransporte(admin.ModelAdmin):
    list_display = ('id_transporte','nu_matricula', 'categoria', 'tipo_transporte')
    list_filter = ('nu_matricula', 'categoria', 'tipo_transporte')
    search_fields = ('nu_matricula', 'categoria', 'tipo_transporte')

#registu model ba admin django
admin.site.register(Transporte, admKombustivelAdminTransporte)

class admKombustivelAdminMotorista(admin.ModelAdmin):
    list_display = ('id_motorista','naran_motorista', 'sexo', 'id_departamentu', 'id_diresaun', 'id_regional')
    list_filter = ('naran_motorista', 'sexo', 'id_departamentu', 'id_diresaun', 'id_regional')
    search_fields = ('naran_motorista', 'sexo', 'id_departamentu', 'id_diresaun', 'id_regional')

#registu model ba admin django
admin.site.register(Motorista, admKombustivelAdminMotorista)

class admKombustivelAdminRegional(admin.ModelAdmin):
    list_display = ('id_regional','naran_regional')
    list_filter = ['naran_regional']
    search_fields = ['naran_regional']

#registu model ba admin django
admin.site.register(Regional, admKombustivelAdminRegional)

class admKombustivelAdminDiresaun(admin.ModelAdmin):
    list_display = ('id_diresaun','naran_diresaun')
    list_filter = ['naran_diresaun']
    search_fields = ['naran_diresaun']

#registu model ba admin django
admin.site.register(Diresaun, admKombustivelAdminDiresaun)

class admKombustivelAdminTinan(admin.ModelAdmin):
    list_display = ['ano']
    list_filter = ['ano']
    search_fields = ['ano']

#registu model ba admin django
admin.site.register(Tinan, admKombustivelAdminTinan)

class admKombustivelAdminDistribuitor(admin.ModelAdmin):
    list_display = ('id_distribuitor', 'naran_distribuitor')
    list_filter = ['naran_distribuitor']
    search_fields = ['naran_distribuitor']

#registu model ba admin django
admin.site.register(Distribuitor, admKombustivelAdminDistribuitor)

class admKombustivelAdminFulan(admin.ModelAdmin):
    list_display = ('id_fulan', 'naran_fulan')
    list_filter = ['naran_fulan']
    search_fields = ['naran_fulan']

#registu model ba admin django
admin.site.register(Fulan, admKombustivelAdminFulan)

class admKombustivelAdminSenhas(admin.ModelAdmin):
    list_display = ('id_senhas', 'nu_senhas', 'folin_senhas')
    list_filter = ('nu_senhas', 'folin_senhas')
    search_fields = ('nu_senhas', 'folin_senhas')

#registu model ba admin django
admin.site.register(Senhas, admKombustivelAdminSenhas)

# class admKombustivelAdminKombustivel(admin.ModelAdmin):
#     list_display = ('id_kombustivel', 'tipo_kombustivel', 'id_distribuitor', 'ano', 'folin_kombustivel', 'data')
#     list_filter = ('tipo_kombustivel', 'id_distribuitor', 'ano', 'folin_kombustivel', 'data')
#     search_fields = ('tipo_kombustivel', 'id_distribuitor', 'ano', 'folin_kombustivel', 'data')

# #registu model ba admin django
# admin.site.register(Kombustivel, admKombustivelAdminKombustivel)

class admKombustivelAdminDistribuisaun(admin.ModelAdmin):
    list_display = ('id_distribuisaun', 'tipo_kombustivel', 'id_transporte', 'id_senhas', 'id_motorista', 'fulan', 'ano', 'destinasaun', 'folin_utilitariu', 'data')
    list_filter = ('tipo_kombustivel', 'id_transporte', 'id_senhas', 'id_motorista', 'fulan', 'ano', 'destinasaun', 'folin_utilitariu', 'data')
    search_fields = ('tipo_kombustivel', 'id_transporte', 'id_senhas', 'id_motorista', 'fulan', 'ano', 'destinasaun', 'folin_utilitariu', 'data')

#registu model ba admin django
admin.site.register(Distribuisaun, admKombustivelAdminDistribuisaun)

class admKombustivelAdminDepartamentu(admin.ModelAdmin):
    list_display = ('id_departamentu', 'naran_departamentu')
    list_filter = ['naran_departamentu']
    search_fields = ['naran_departamentu']
#registu model ba admin django
admin.site.register(Departamentu, admKombustivelAdminDepartamentu)