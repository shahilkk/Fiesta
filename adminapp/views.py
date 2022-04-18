from django.shortcuts import render

# Create your views here.


def master(req):
    return render(req,'master.html')

def index(req):
    return render(req,'index.html')  

def customer(req):
    return render(req,'customer.html') 


def addcustomer(req):
    return render(req,'addcustomer.html')  


def Estimate(req):
    return render(req,'Estimate.html')    


def invoicegrid(req):
    return render(req,'invoicegrid.html')        