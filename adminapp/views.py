from django.shortcuts import render

# Create your views here.


def master(req):
    return render(req,'master.html')

def index(req):
    return render(req,'index.html')  

def customer(req):
    return render(req,'customer.html')


def marketingstaff(req):
    return render(req,'marketingstaff.html')      


def addcustomer(req):
    return render(req,'addcustomer.html')  


def Estimate(req):
    return render(req,'Estimate.html')    


def invoicegrid(req):
    return render(req,'invoicegrid.html')        
  

def invoiceList(req):
    return render(req,'invoiceList.html') 


def addinvoice(req):
    return render(req,'addinvoice.html')


def invoicedetails(req):
    return render(req,'invoicedetails.html') 


def editinvoice(req):
    return render(req,'editinvoice.html') 


def invoicesettings(req):
    return render(req,'invoicesettings.html') 

def products(req):
    return render(req,'products.html') 



def editestimate(req):
    return render(req,'editestimate.html')    



def payment(req):
    return render(req,'payment.html')  


def addpayment(req):
    return render(req,'addpayment.html')   



def expenses(req):
    return render(req,'expenses.html')          



def addexpenses(req):
    return render(req,'addexpence.html')



def profit(req):
    return render(req,'profit.html')          



def addprofit(req):
    return render(req,'addprofit.html')



def addestimate(req):
    return render(req,'addestimate.html')    

    
def editcustomer(req):
    return render(req,'editcustomer.html')

def calender(req):
    return render(req,'calender.html')


def banksettings(req):
    return render(req,'banksettings.html')
      
