from django.urls import path
from . import views


urlpatterns = [
    path('master',views.master,name="master"),
    path('index',views.index,name="index"),
    path('customer',views.customer,name="customer"),
    path('addcustomer',views.addcustomer,name="addcustomer"),
    path('marketingstaff',views.marketingstaff,name="marketingstaff"),
    path('estimate',views.Estimate,name="estimate"),
    path('invoicegrid',views.invoicegrid,name="invoicegrid"),
    path('invoiceList',views.invoiceList,name="invoiceList"),
    path('editinvoice',views.editinvoice,name="editinvoice"),
    path('addinvoice',views.addinvoice,name="addinvoice"),
    path('invoicedetails',views.invoicedetails,name="invoicedetails"),
    path('invoicesettings',views.invoicesettings,name="invoicesettings"),


]