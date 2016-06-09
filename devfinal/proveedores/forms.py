from django import forms
from .models import Proveedor, Startup, Categoria

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'descripcion', 'pagina_web','logo', 'categoria','direccion']

class StartupForm(forms.ModelForm):
	class Meta:
		model = Startup
		fields = ['nombre', 'descripcion','pagina_web','logo', 'proveedores', 'direccion']