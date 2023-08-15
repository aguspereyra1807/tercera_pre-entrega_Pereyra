from django import forms

class InstrumentForm(forms.Form):
    type = forms.CharField(max_length=20, required=True)
    model = forms.CharField(max_length=50, required=True)
    price = forms.IntegerField(required=True)
    inStock = forms.BooleanField(required=False)

class ClientForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)
    lastname = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=50, required=True) 
    
class BranchForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    province = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=50, required=True)