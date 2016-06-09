from rest_framework import serializers
from ..models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proveedor
		fields = ('nombre', 'descripcion', 'pagina_web', 'logo','categoria', 'direccion','latLng')