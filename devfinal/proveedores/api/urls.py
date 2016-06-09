from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^prov/(?P<pk>\d+)/$',
		views.ProveedorDetailView.as_view(),
		name="prov_detalle"),
]