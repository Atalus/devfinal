from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Proveedor, Startup
from .forms import ProveedorForm, StartupForm
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class HomeView(View):
    def get(self, request):
        template_name = "proveedores/proveedores.html"
        form1 = ProveedorForm()
        form2 = StartupForm()
        provedores = Proveedor.objects.all()
        startups = Startup.objects.all()
        context = {
            'form1': form1,
            'form2': form2,
            'proveedores': provedores,
            'startups': startups,
        }
        return render(request, template_name, context)

    def post(self, request):
        if request.POST.get("formType", "") == "servicio":
            form = ProveedorForm(request.POST, request.FILES)
        else:
            form = StartupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gracias por compartir con la comunidad emprendedora')
        else:
            messages.error(request, 'Oops... ¡algo falló! ¿Podrías intentar de nuevo?')
        return redirect('homeview')

class ProveView(View):
    def get(self, request):
        idProv = request.GET.get("id")
        template_name = "proveedores/proveedor.html"
        proveedor = Proveedor.objects.get(id=idProv)
        context = {
        'proveedor': proveedor,
        }
        return render(request, template_name, context)


#class HomeStartups(View):
#    def get(self, request):
#        template_name = "startups/startups.html"
#        form1 = StartupForm()
#        startups = 

class FacebookBotView(View):
    def get(self, request):
        print(request.GET)
        if request.GET.get("hub.verify_token") == "123hector":
            return HttpResponse(request.GET.get("hub.challenge",  "nada"))
        else:
            return HttpResponseNotFound("not found")
    @method_decorator(csrf_exempt)
    def post(self, request):
        print(request.POST)