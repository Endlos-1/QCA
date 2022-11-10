from re import template
from django.shortcuts import render
from home.models import AmountRequest

# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def agent_Faq(request):
    return render(request, 'home/agentFaq.html')

def broker_Faq(request):
    return render(request, 'home/brokerFaq.html')

def applynow(request):
    if request.method=="POST":
        amount =request.POST['amount']
        email=request.POST['email']
        print(amount,email)
        print("This  is Post")
        ins = AmountRequest(amount=amount,mail=email)
        ins.save()
    return render(request, 'home/applynow.html')


def contactUs(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name,phone,subject,message)

    return render(request, 'home/contactUs.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')

def howit(request):
    return render(request, 'home/howitworks.html')

def whyadvance(request):
    return render(request, 'home/whycommissionadvance.html')

def thanks(request):
    return render(request, 'home/thankyou.html')