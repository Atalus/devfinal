from django.apps import AppConfig
from django.contrib import algoliasearch
from .index import CategoriaIndex, ProveedorIndex, StartupIndex


class ProveedoresConfig(AppConfig):
    name = 'proveedores'
        
    def ready(self):
        Categoria = self.get_model('categoria')
        Proveedor = self.get_model('proveedor')
        Startup = self.get_model('startup')
        algoliasearch.register(Categoria, CategoriaIndex)
        algoliasearch.register(Proveedor, ProveedorIndex)
        algoliasearch.register(Startup, StartupIndex)