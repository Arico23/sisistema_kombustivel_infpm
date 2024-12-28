from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django.views.generic import CreateView
from django import forms
import pprint
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from pprint import pprint

#formulario distribuitor
class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distribuitor
        fields = ['naran_distribuitor', 'montante_distribuitor', 'data', 'ano']
        labels = {
             'naran_distribuitor': 'Naran Distributor',
             'montante_distribuitor': 'Montante Kombustivel',
             'data': 'Data Simu Kombustivel',
             'ano': 'Tinan',
        # fields = ['cutomer'] #only specific form
        }
        widgets = {
            'data': forms.TextInput(attrs={'readonly': 'readonly', 'style': 'background-color: lightgray;'})
        }
        
    def save(self, commit=True):
        instance = super(DistributorForm, self).save(commit=False)
        montante_distribuitor = self.cleaned_data.get('montante_distribuitor')
        # Calculate montante_atual based on montante_distribuitor
        instance.montante_atual = montante_distribuitor  # Example calculation
        if commit:
            instance.save()
        return instance

#formulario senhas
class SenhasForm(forms.ModelForm):
    class Meta:
        model = Senhas
        fields = ['nu_senhas', 'folin_senhas', 'id_distributor']
        labels = {
            'nu_senhas': 'Numeru Senhas',
            'folin_senhas': 'Folin Senhas',
            'id_distributor': 'Distributor'
        }
        placeholder = {
            'nu_senhas': 'prense numeru senhas',
            'folin senhas': 'prense numeru senhas'  
        }
    
    def clean(self):
        cleaned_data = super().clean()
        folin_senhas = cleaned_data.get('folin_senhas')
        id_distributor = cleaned_data.get('id_distributor')
        

        if id_distributor and folin_senhas is not None:
            # Retrieve the related Distributor instance
            distributor = Distribuitor.objects.get(id_distribuitor=id_distributor.id_distribuitor)
            
            # Check if folin_senhas is below montante_senhas
            if folin_senhas > distributor.montante_atual:
                raise ValidationError(
                    f'Folin Senhas ({folin_senhas}) labele menus liu husi montante atual ({distributor.montante_atual}) husi distributor neebe hili.'
                )

        return cleaned_data
        


#formulario Regional
class RegionalForm(forms.ModelForm):
    class Meta:
        model = Regional
        fields = ['naran_regional']
        labels = {
             'naran_regional': 'Naran Regional',
        # fields = ['cutomer'] #only specific form
        }

#formulario Departamentu
class DepartamentuForm(forms.ModelForm):
    class Meta:
        model = Departamentu
        fields = ['naran_departamentu']
        labels = {
             'naran_departamentu': 'Naran Departamentu'
        # fields = ['cutomer'] #only specific form
        }
#formulario Diresaun
class DiresaunForm(forms.ModelForm):
    class Meta:
        model = Diresaun
        fields = ['naran_diresaun']
        labels = {
             'naran_diresaun': 'Naran Diresaun',
        # fields = ['cutomer'] #only specific form
        }
#formulario Fulan
class FulanForm(forms.ModelForm):
    class Meta:
        model = Fulan
        fields = ['naran_fulan']
        labels = {
             'naran_fulan': 'Fulan',
        # fields = ['cutomer'] #only specific form
        }

#formulario Fulan
class TinanForm(forms.ModelForm):
    class Meta:
        model = Tinan
        fields = ['ano']
        labels = {
             'ano': 'Tinan',
        # fields = ['cutomer'] #only specific form
        }

#formulario Motorista
class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['naran_motorista', 'sexo', 'id_diresaun', 'id_departamentu', 'id_regional']
        labels = {
             'id_diresaun': 'Diresaun',
             'id_departamentu': 'Departamentu',
             'id_regional': 'Regional',
        # fields = ['cutomer'] #only specific form
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['naran_motorista'].required = True
            self.fields['sexo'].required = True
            self.fields['id_departamentu'].required = False
            self.fields['id_diresaun'].required = True 
            self.fields['id_regional'].required = True
            self.helper.layout = Layout(
                Row(
                    Column('naran_motorista', css_class='form-group col-md-6 mb-0'),
                    Column('sexo', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('id_departamentu', css_class='form-group col-md-6 mb-0'),
                    Column('id_diresaun', css_class='form-group col-md-6 mb-0'),
                    Column('id_regional', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Rai Dadus</i></button> """),
                HTML(""" <span class="btn btn-sm btn-danger"  onclick=self.history.back()></i>Kansela</span></div> """)
            ) 
             
#formulario distribuisaun kombustivel
class DistribuisaunForm(forms.ModelForm):
    class Meta:
        model = Distribuisaun
        fields = ['tipo_kombustivel', 'kilometrajen', 'id_transporte', 'id_senhas', 'id_motorista','fulan', 'ano', 'destinasaun', 'folin_utilitariu', 'data']
        labels = {
             'tipo_kombustivel': 'Tipu Kombustivel',
             'kilomtrajen': 'Kilometrajen',
             'id_transporte' : 'Transporte',
             'id_senhas': 'Folin Senhas',
             'id_motorista': 'Motorista',
             'id_diresaun': 'Diresaun',
             'id_departamentu': 'Departamentu',
             'id_motorista': 'Naran Motorista',
             'ano' : 'Tinan',
             'fulan' : 'Fulan',
             'data' : 'Data Foti Senhas',
             'folin_utilitariu' : 'Folin Unitariu',
             
        }
     

        widgets = {
            # 'data': forms.TextInput(attrs={'readonly': 'readonly', 'style': 'background-color: lightgray;'})
            'data': forms.TextInput(attrs={'type': 'date'}),
        } 
     
        # fields = ['cutomer'] #only specific form
    
   
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['tipo_kombustivel'].required = True
            self.fields['kilometrajen'].required = False
            self.fields['id_transporte'].required = True
            self.fields['id_senhas'].required = True
            self.fields['id_motorista'].required = True
            self.fields['fulan'].required = True
            self.fields['ano'].required = True
            self.fields['destinasaun'].required = True
            self.fields['data'].required = True
            self.fields['folin_utilitariu'].required = False

            # Filter the choices for the related field to only show Senhas with status as "non-distributed"
            self.fields['id_senhas'].queryset = Senhas.objects.filter(status='Seidauk Distribui')

            self.helper.layout = Layout(
                Row(
                    Column('tipo_kombustivel', css_class='form-group col-md-6 mb-0'),
                    Column('kilometrajen', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('id_transporte', css_class='form-group col-md-6 mb-0'),
                    Column('id_senhas', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('id_motorista', css_class='form-group col-md-6 mb-0'),
                    Column('fulan', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('ano', css_class='form-group col-md-6 mb-0'),
                    Column('destinasaun', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('folin_utilitariu', css_class='form-group col-md-6 mb-0'),
                    Column('data', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                HTML(""" <center> <img id='output' width='200' /> </center> """),
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Rai Dadus</i></button> """),
                HTML(""" <span class="btn btn-sm btn-danger"  onclick=self.history.back()>Kansela</span></div> """)
            )

    def save(self, commit=True):
        instance = super(DistribuisaunForm, self).save(commit=False)
        
        # Update the status of the related Senhas object to "distributed"
        senhas_instance = instance.id_senhas
        senhas_instance.status = 'Distribui ona'
        distributor_instance = instance.id_senhas.id_distributor
        distributor_instance.montante_atual = distributor_instance.montante_atual - senhas_instance.folin_senhas
        senhas_instance.save()
        distributor_instance.save()
        
        if commit:
            instance.save()
        
        return instance

#formulario transporte
class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['nu_matricula', 'categoria', 'tipo_transporte']
        labels = {
             'nu_matrikula': 'Numeru Matrikula Transporte',
             'categoria' : 'Kategoria Transporte',
             'tipo_transporte' : 'Modelu Transporte',
        }
        # fields = ['cutomer'] #only specific form
        
        
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['nu_matricula'].required = False
            self.fields['categoria'].required = True
            self.fields['tipo_transporte'].required = True
    #         self.helper.layout = Layout(
    #             Row(
    #                 Column('nu_matricula', css_class='form-group col-md-6 mb-0'),
    #                 Column('categoria', css_class='form-group col-md-6 mb-0'),
    #                 Column('tipo_transporte', css_class='form-group col-md-6 mb-0'),
    #                 css_class='form-row'
    #             ),
    #             HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
    #             HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
    #         )



# class DistribuisaunForm(ModelForm):
#     class Meta:
#         model = Distribuisaun
#         fields =  '__all__' #all field in the models
#         # fields = ['cutomer'] #only specific form


# Form to change username and password of utilizador
class UserProfileForm(forms.ModelForm):
    old_password = forms.CharField(label='Password Tuan', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password Foun'
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].required = True
        self.fields['password'].required = True
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('old_password', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('password', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Renova <i class="fa fa-save"></i></button> """),
            HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i>Kansela</span></div> """)
        )
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Add password validation logic here if needed
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise forms.ValidationError('Password Tuan Sala.')
        return cleaned_data
    
    def save(self, commit=True):
        instance = super(UserProfileForm, self).save(commit=False)
        
        # Update the username and password of the utilizador object
        instance.username = self.cleaned_data['username']
        instance.set_password(self.cleaned_data['password'])
        
        if commit:
            instance.save()
        
        return instance
# myapp/forms.py
from django import forms




    
    
