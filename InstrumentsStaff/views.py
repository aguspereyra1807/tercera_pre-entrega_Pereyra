from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from InstrumentsApp.models import *
def staffHome(request):
    return render(request, "D:/CODERHOUSE Python/Pre-entrega III/Instrument4Sale/InstrumentsStaff/templates/stafftemplates/home.html")

def addInstrument(request):
    if request.method == "POST":
        formulario = InstrumentForm(request.POST)
        if formulario.is_valid():
            instrument_type = formulario.cleaned_data.get('type')
            instrument_model = formulario.cleaned_data.get('model')
            instrument_price = formulario.cleaned_data.get('price')
            instrument_instock = formulario.cleaned_data.get('inStock')
            instrument = Instrument(type = instrument_type, 
                          model = instrument_model, 
                          price = instrument_price,
                          inStock = instrument_instock) 
            instrument.save()
            return render(request, "stafftemplates/home.html")
    else: 
        formulario = InstrumentForm()
    return render(request, "stafftemplates/instruments_add.html", {"form": formulario})

def addClient(request):
    if request.method == "POST":
        formulario = ClientForm(request.POST)
        if formulario.is_valid():
            client_name = formulario.cleaned_data.get('name')
            client_lastname = formulario.cleaned_data.get('lastname')
            client_email = formulario.cleaned_data.get('email')
            client = Client(name = client_name, 
                          lastname = client_lastname, 
                          email = client_email)
            client.save()
            return render(request, "stafftemplates/home.html")
    else: 
        formulario = ClientForm() 
    return render(request, "stafftemplates/clients_add.html", {"form": formulario})

def addBranch(request):
    if request.method == "POST":
        formulario = BranchForm(request.POST)
        if formulario.is_valid():
            branch_name = formulario.cleaned_data.get('name')
            branch_province = formulario.cleaned_data.get('province')
            branch_address = formulario.cleaned_data.get('address')
            branch = Branch(name = branch_name, 
                          province = branch_province, 
                          address = branch_address)
            branch.save()
            return render(request, "stafftemplates/home.html")
    else: 
        formulario = BranchForm() 
    return render(request, "stafftemplates/branchs_add.html", {"form": formulario})