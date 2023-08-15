from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsApp/templates/apptemplates/home.html")

def instrumentsView(request):
    context = {'models' : Instrument.objects.all()}
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsApp/templates/apptemplates/instruments_view.html", context)

def branchsView(request):
    context = {'branchs' : Branch.objects.all()}
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsApp/templates/apptemplates/branchs_view.html", context )

def clientsView(request):
    context = {'clients' : Client.objects.all()}
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsApp/templates/apptemplates/client_view.html", context )

def aboutUs(request):
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsApp/templates/apptemplates/about_us.html" )

#===================================================================================================================================================================

#Búsquedas


def instrumentSearch(request):
    if request.GET['search']: 
        patron = request.GET['search']
        modelos = Instrument.objects.filter(model__icontains=patron) 
        contexto = {'models': modelos} 
        return render(request, "apptemplates/instruments_view.html", contexto )
    return render(request, "apptemplates/instruments_view.html")

def clientSearch(request):
    if request.GET['search']: 
        patron = request.GET['search']
        nombres = Client.objects.filter(name__icontains=patron) 
        contexto = {'clients': nombres} 
        return render(request, "apptemplates/client_view.html", contexto )
    return render(request, "apptemplates/client_view.html")

def branchSearch(request):
    if request.GET['search']: 
        patron = request.GET['search']
        nombres = Branch.objects.filter(name__icontains=patron) 
        contexto = {'branchs': nombres} 
        return render(request, "apptemplates/branchs_view.html", contexto )
    return render(request, "apptemplates/branchs_view.html")