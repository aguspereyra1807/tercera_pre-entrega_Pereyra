from django.urls import path, include
from .views import *
urlpatterns = [
    path('home/', home ,name="home"),
    path('instruments/', instrumentsView, name="instruments"),
    path('brachs/', branchsView, name="branchs"),
    path('about_us/', aboutUs, name="about_us"),
    path('clients/', clientsView, name="clients"),  
    path('instruments_search/', instrumentSearch, name="instruments_search"),
    path('client_search/', clientSearch, name="client_search"),
    path('branch_search/', branchSearch, name="branch_search"),
   path('staff/', include("InstrumentsStaff.urls")),
   
]
