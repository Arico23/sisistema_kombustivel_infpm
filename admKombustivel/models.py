from datetime import date
from django.db import models

class Utilizador(models.Model):
      
    LEVEL = (
            ('admin', 'admin'),
            ('user', 'user'))
        
    id_user = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices = LEVEL)

    def __str__(self):
        return self.username
    
class Transporte(models.Model):
    KATEGORY = (
        ('Kareta', 'Kareta'),
        ('Motor', 'Motor'),
        ('Forklif', 'Forklif'))
        
    id_transporte = models.AutoField(primary_key=True, editable=False)
    nu_matricula = models.CharField(max_length=10)
    categoria = models.CharField(max_length=20, choices = KATEGORY)
    tipo_transporte = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_transporte
        
    
class Regional(models.Model):     
    id_regional = models.AutoField(primary_key=True, editable=False)
    naran_regional = models.CharField(max_length=200)
    

    def __str__(self):
        return self. naran_regional
    
class Departamentu(models.Model):     
    id_departamentu = models.AutoField(primary_key=True, editable=False)
    naran_departamentu = models.CharField(max_length=200)
    

    def __str__(self):
        return self.naran_departamentu

 #Models Diresaun   
class Diresaun(models.Model):     
    id_diresaun = models.AutoField(primary_key=True, editable=False)
    naran_diresaun = models.CharField(max_length=200)
    

    def __str__(self):
        return self.naran_diresaun
#Models Motorista
class Motorista(models.Model):
    SEXO = (
        ('Feto', 'Feto'),
        ('Mane', 'Mane'))
        
    id_motorista = models.AutoField(primary_key=True, editable=False)
    naran_motorista = models.CharField(max_length=200)
    sexo = models.CharField(max_length=20, choices = SEXO)
    id_departamentu = models.ForeignKey(Departamentu, on_delete=models.CASCADE, null=False, blank=False)
    id_diresaun = models.ForeignKey(Diresaun, on_delete=models.CASCADE, null=False, blank=False)
    id_regional = models.ForeignKey(Regional, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self. naran_motorista


#models tinan    
class Tinan(models.Model):     
    ano = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return str(self.ano) 
 #models distributor   
class Distribuitor(models.Model):     
    id_distribuitor = models.AutoField(primary_key=True, editable=False)
    naran_distribuitor = models.CharField(max_length=200)
    montante_distribuitor = models.FloatField(default=0) 
    montante_atual = models.FloatField(default=0) 
    data = models.DateField(default=date.today)
    ano = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.naran_distribuitor
    
class Fulan(models.Model):     
    id_fulan = models.AutoField(primary_key=True, editable=False)
    naran_fulan = models.CharField(max_length=20)
    
    def __str__(self):
        return self.naran_fulan

class Senhas(models.Model):
    STATUS = (
        ('Seidauk Distribui', 'Seidauk Distribui'),
        ('Distribui Ona', 'Distribui Ona'))
    id_senhas = models.AutoField(primary_key=True, editable=False)
    nu_senhas = models.CharField(max_length=200)
    folin_senhas = models.FloatField(default=0)
    status = models.CharField(max_length=20 ,choices = STATUS, default='Seidauk Distribui')
    
    def __int__(self):
        return self.id_senhas
    
    def __str__(self):
         return f'({self.nu_senhas}) - (${self.folin_senhas})'
    # def __str__(self):
    #     return f'Kompania: ({self.id_distribuitor.naran_distribuitor}) , Kodigu Senhas: ({self.nu_senhas}), Folin: (${self.folin_senhas})'
    
# class Kombustivel(models.Model):
#     KATEGORY = (
#         ('Gazolina', 'Gazolina'),
#         ('Gazoel', 'Gazoel'))   
    
#     id_kombustivel= models.AutoField(primary_key=True, editable=False)
#     tipo_kombustivel = models.CharField(max_length=20, choices = KATEGORY)
#     id_distribuitor = models.ForeignKey(Distribuitor, on_delete=models.CASCADE, null=True, blank=True)
#     ano = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=False, blank=False)
#     folin_kombustivel = models.FloatField(default=0)
#     data = models.DateField(default=date.today)
  
#     def __str__(self):
#         return f'{self.id_distribuitor.naran_distribuitor} - {self.tipo_kombustivel}'
    
class Distribuisaun(models.Model):
    KATEGORY = (
        ('Gazolina', 'Gazolina'),
        ('Gazoel', 'Gazoel'))   
         
    id_distribuisaun = models.AutoField(primary_key=True, editable=False)
    tipo_kombustivel = models.CharField(max_length=20, choices = KATEGORY)
    kilometrajen = models.CharField(max_length=200, default=0)   
    id_transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, null=False, blank=False)
    id_senhas = models.ForeignKey(Senhas, on_delete=models.CASCADE, null=False, blank=False)
    id_motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, null=False, blank=False)
    fulan = models.ForeignKey(Fulan, on_delete=models.CASCADE, null=False, blank=False)
    ano = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=False, blank=False)
    destinasaun = models.CharField(max_length=200)
    folin_utilitariu = models.FloatField(max_length=200)
    data = models.DateField(default=date.today)
   
    def __str__(self):
        return self.id_senhas.nu_senhas
