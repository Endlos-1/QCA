from re import template
from django.shortcuts import render
from home.models import AmountRequest,RemainingFormRecords,Agent
from home.models import ContactUs
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def agent_Faq(request):
    return render(request, 'home/agentFaq.html')

def broker_Faq(request):
    return render(request, 'home/brokerFaq.html')

@login_required(login_url='accounts:signin')
def applynow(request):
    if request.method=="POST" and 'HomeFormButton' in request.POST:
        amount =request.POST['amount']
        email=request.POST['email']
        print(amount,email)
        print("This  is Post")
        ins = AmountRequest(amount=amount,mail=email)
        ins.save()

    if request.method=="POST" and 'ContactButton' in request.POST:
       BrokerRecordOfCompany=request.POST['BrokerRecordOfCompany']
       OpenAdvanceswihOther=request.POST['OpenAdvanceswihOther']
       Agent_First_Name=request.POST['Agent_First_Name']
       Agent_Last_Name=request.POST['Agent_Last_Name']
       Agent_City=request.POST['Agent_City']
       Agent_State=request.POST['Agent_State']
       Agent_Zip=request.POST['Agent_Zip']
       Agent_Cell_Phone=request.POST['Agent_Cell_Phone']
       print(BrokerRecordOfCompany)
       ins=RemainingFormRecords(BrokerRecordOfCompany=BrokerRecordOfCompany, OpenAdvanceswihOther=OpenAdvanceswihOther)
       ins=Agent( Agent_First_Name= Agent_First_Name,  Agent_Last_Name= Agent_Last_Name,Agent_City=Agent_City,Agent_State=Agent_State,Agent_Zip=Agent_Zip,Agent_Cell_Phone=Agent_Cell_Phone
       )
       ins.save()
    return render(request, 'home/applynow.html')

def contactUs(request):
    return render(request, 'home/contactUs.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')

def howit(request):
    return render(request, 'home/howitworks.html')

def whyadvance(request):
    return render(request, 'home/whycommissionadvance.html')

def thanks(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        print(name,phone,subject,message)
        print("This is contact us post")
        ins = ContactUs(Name=name,Phone=phone,Subject=subject,Message=message)
        ins.save()
    return render(request, 'home/thankyou.html')