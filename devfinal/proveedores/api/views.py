from rest_framework import generics
from ..models import Proveedor
from .serializers import ProveedorSerializer

class ProveedorDetailView(generics.RetrieveAPIView):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorSerializer