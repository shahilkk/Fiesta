from django.urls import path
from . import views


urlpatterns = [
    path('master',views.master,name="master"),
    path('index',views.index,name="index"),
    path('customer',views.customer,name="customer"),
    path('addcustomer',views.addcustomer,name="addcustomer"),

]