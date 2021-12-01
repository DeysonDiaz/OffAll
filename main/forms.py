from django import forms
from .models import Client, Profession, Professional
from django.forms import ModelChoiceField

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = [
			'names',
			'surnames',
			'email',
			'password',
			'telephone',
			'dni',
            'date',
		]
class RawClientForm(forms.Form):
    names  = forms.CharField(label = 'Nombres')
    surnames = forms.CharField(label = 'Apellidos')
    email = forms.EmailField(label = 'Correo')
    password = forms.CharField(label = 'Contraseña')
    telephone = forms.IntegerField(label = 'Telefono')
    dni = forms.IntegerField(label = 'DNI')
    date = forms.DateField(label = 'Fecha')

class ProfessionalForm(forms.ModelForm):
	class Meta:
		model = Professional
		fields = [
			'names',
			'surnames',
			'email',
			'password',
			'telephone',
			'dni',
            'date',
            'profession',
			'img',
            'description',
		]
class RawProfessionalForm(forms.Form):
    names  = forms.CharField(label = 'Nombres')
    surnames = forms.CharField(label = 'Apellidos')
    email = forms.EmailField(label = 'Correo')
    password = forms.CharField(label = 'Contraseña')
    telephone = forms.IntegerField(label = 'Telefono')
    dni = forms.IntegerField(label = 'DNI')
    date = forms.DateField(label = 'Fecha')
    profession = forms.ModelChoiceField(queryset = Profession.objects.all())
    img = forms.ImageField(label = 'Seleccionar Imagen')
    description = forms.CharField(label = 'Descripcion',
	widget = forms.Textarea(
			attrs = {
			'placeholder': 'Escriba una descripcion detallada, por favor',
			'id': 'nombreID',
			'class': 'special',
			'cols': '30',
			}

		)
	)