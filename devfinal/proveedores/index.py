from django.contrib.algoliasearch import AlgoliaIndex

class CategoriaIndex(AlgoliaIndex):
    fields = ('nombre', 'descripcion')
    settings = {'attributesToIndex': ['nombre', 'descripcion']}

class ProveedorIndex(AlgoliaIndex):
    fields = ('nombre', 'descripcion')
    settings = {'attributesToIndex': ['nombre', 'descripcion']}

class StartupIndex(AlgoliaIndex):
    fields = ('nombre', 'descripcion')
    settings = {'attributesToIndex': ['nombre', 'descripcion']}