from django.urls import path
from .views import *

app_name = 'InstrumentsStaff'

urlpatterns = [
    path('', staffHome , name="staffHome"),
    path('add_instrument', addInstrument, name="add_instrument"),
    path('add_client', addClient, name="add_client"),
    path('add_branch', addBranch, name="add_branch"),

]
