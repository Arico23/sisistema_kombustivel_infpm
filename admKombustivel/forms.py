from django.forms import ModelForm
from django.views.generic import CreateView
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML

#formulario distribuitor
class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distribuitor
        fields = ['naran_distribuitor']
        labels = {
             'naran_distribuitor': 'Naran Distributor',
        # fields = ['cutomer'] #only specific form
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['naran_distributor'].required = True
            self.helper.layout = Layout(
                Row(
                    Column('naran_distributor', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
                HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
            )

#formulario Motorista
class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ['naran_motorista', 'sexo', 'id_diresaun', 'id_departamentu', 'id_regional']
        # labels = {
        #      'naran_motorista': 'sexo',
        # # fields = ['cutomer'] #only specific form
        # }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['naran_motorista'].required = True
            self.fields['sexo'].required = True
            self.fields['id_departamentu'].required = True
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
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
                HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
            )

#formulaio stock kombustivel
# class KombustivelForm(forms.ModelForm):
#     class Meta:
#         model = Kombustivel
#         fields = ['tipo_kombustivel', 'id_distribuitor', 'ano', 'folin_kombustivel', 'data']
#         labels = {
#              'tipo_kombustivel': 'Tipu Kombustivel',
#              'id_distribuitor' : 'Distributor',
#              'ano' : 'Tinan',
#              'folin_kombustivel' : 'Folin Senhas ($)',
#              'data': 'Loron Ohin'
#         }
#         # fields = ['cutomer'] #only specific form
    
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.helper = FormHelper()
#             self.fields['tipo_kombustivel'].required = True
#             self.fields['id_distribuitor'].required = True
#             self.fields['ano'].required = True
#             self.fields['folin_kombustivel'].required = True
#             self.fields['data'].required = True
#             self.helper.layout = Layout(
#                 Row(
#                     Column('tipo_kombustivel', css_class='form-group col-md-6 mb-0'),
#                     Column('id_distribuitor', css_class='form-group col-md-6 mb-0'),
#                     css_class='form-row'
#                 ),
#                 Row(
#                     Column('ano', css_class='form-group col-md-6 mb-0'),
#                     Column('folin_kombustivel', css_class='form-group col-md-6 mb-0'),
#                     Column('data', css_class='form-group col-md-6 mb-0'),
#                     css_class='form-row'
#                 ),
#                 HTML(""" <center> <img id='output' width='200' /> </center> """),
#                 HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
#                 HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
#             )
#formulario distribuisaun kombustivel
class DistribuisaunForm(forms.ModelForm):
    class Meta:
        model = Distribuisaun
        fields = ['tipo_kombustivel', 'id_transporte', 'id_senhas', 'id_motorista','fulan', 'ano', 'destinasaun', 'folin_utilitariu', 'data']
        labels = {
             'tipo_kombustivel': 'Tipu Kombustivel',
             'id_transporte' : 'Transporte',
             'id_senhas': 'Numeru Senhas',
             'id_motorista': 'Motorista',
             'id_diresaun': 'Diresaun',
             'id_departamentu': 'Departamentu',
             'id_motorista': 'Naran Motorista',
             'ano' : 'Tinan',
             'fulan' : 'Fulan',
             'data' : 'Loron Ohin'
        }
     
        # fields = ['cutomer'] #only specific form
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.fields['tipo_kombustivel'].required = True
            self.fields['id_transporte'].required = True
            self.fields['id_senhas'].required = True
            self.fields['id_motorista'].required = True
            self.fields['fulan'].required = True
            self.fields['ano'].required = True
            self.fields['destinasaun'].required = True
            self.fields['data'].required = True


            self.helper.layout = Layout(
                Row(
                    Column('id_kombustivel', css_class='form-group col-md-6 mb-0'),
                    Column('id_transporte', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('id_senhas', css_class='form-group col-md-6 mb-0'),
                    Column('id_diresaun', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('id_departamentu', css_class='form-group col-md-6 mb-0'),
                    Column('id_motorista', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('fulan', css_class='form-group col-md-6 mb-0'),
                    Column('ano', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('destinasaun', css_class='form-group col-md-6 mb-0'),
                    Column('data', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                HTML(""" <center> <img id='output' width='200' /> </center> """),
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
                HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
            )

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
            self.fields['nu_matricula'].required = True
            self.fields['categoria'].required = True
            self.fields['tipo_transporte'].required = True
            self.helper.layout = Layout(
                Row(
                    Column('nu_matricula', css_class='form-group col-md-6 mb-0'),
                    Column('categoria', css_class='form-group col-md-6 mb-0'),
                    Column('tipo_transporte', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-info" type="submit">Save <i class="fa fa-save"></i></button> """),
                HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
            )



# class DistribuisaunForm(ModelForm):
#     class Meta:
#         model = Distribuisaun
#         fields =  '__all__' #all field in the models
#         # fields = ['cutomer'] #only specific form

    
    
