from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Comuna, Region, Inmuebles


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = "Nombre"
    last_name = forms.CharField()
    last_name.label = "Apellido"
    email = forms.EmailField()

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        labels = {'username': _("Nombre de Usuario")}


class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'), (2, 'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(max_length=12, label='Rut')
    direccion = forms.CharField(max_length=100, label='Direccion')
    telefono = forms.CharField(max_length=20, label='Teléfono')
    correo = forms.CharField(max_length=30, label='Correo Electrónico')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Nombre',
                  'last_name': 'Apellido', 'email': 'Email'}


class InmuebleForm(forms.Form):
    tipos = ((1, "Casa"), (2, "Departamento"), (3, "Parcela"),
             (4, "Estacionamiento"), (5, "Otro"))
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas = [(x.id, x.comuna) for x in list(Comuna.objects.filter())]

    def nombre_comuna(e):
        return e[1]
    comunas.sort(key=nombre_comuna)

    id_comuna = forms.ChoiceField(choices=comunas)
    regiones = [(x.id, x.region) for x in list(Region.objects.filter())]
    id_region = forms.ChoiceField(choices=regiones)
    nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(
        label='Descripción del Inmueble', max_length=100)
    m2_construido = forms.CharField(label='M2 Contruido', max_length=100)
    numero_banos = forms.CharField(label='Numero de Baños', max_length=100)
    direccion = forms.CharField(label='Direccion', max_length=100)
    m2_terreno = forms.CharField(label='M2 de Terreno', max_length=100)
    numero_est = forms.CharField(
        label='Núm. de Estacionamientos', max_length=100)
    precio = forms.CharField(label='Precio', max_length=100)


class InmuebleUpdateForm(forms.ModelForm):
    class Meta:
        model = Inmuebles
        fields = ['nombre_inmueble', 'descripcion', 'm2_construido',
                  'numero_banos', 'direccion', 'm2_terreno', 'numero_est', 'precio']
