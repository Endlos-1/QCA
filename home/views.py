from re import template
from accounts.models import User
from django.shortcuts import render,redirect
from home.models import AmountRequest,RemainingFormRecords,Agent,Property,Broker,AgentBankDetails
from home.models import ContactUs,SalesInformation_AgentDetail,ClosingCompanyDetails,Documents
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
    if request.method=="POST" and 'HomeFormButton':
        amount =request.POST['amount']
        email = request.POST['email']
        mail = email
        amount=amount.replace('$', '')
        amount=amount.replace(',', '')
        amount=int(amount)
        
    
        if User.objects.filter(email=mail).exists() and request.user.is_authenticated:
            return redirect('home:applynow')
        elif User.objects.filter(email=mail).exists():
            return redirect('accounts:signin?next={{request.home:applynow}}')
        else:
            return redirect('accounts:register')
        print(amount,email)
        print("This  is Post")
        ins = AmountRequest(amount=amount,mail=email)
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
        Name=request.POST['Name']
        Phone=request.POST['Phone']
        Subject=request.POST['Subject']
        Message=request.POST['Message']
        print(Name,Phone,Subject,Message)
        print("This is contact us post")
        ins = ContactUs(Name=Name,Phone=Phone,Subject=Subject,Message=Message)
        ins.save()
    return render(request, 'home/thankyou.html')


def SalesInfoForm(request):
    if request.method=="POST":
       BrokerRecordOfCompany=request.POST['BrokerRecordOfCompany']
       OpenAdvanceswihOther=request.POST['OpenAdvanceswihOther']
       Agent_First_Name=request.POST['Agent_First_Name']
       Agent_Last_Name=request.POST['Agent_Last_Name']
       Agent_Home_address=request.POST['Agent_Home_address']
       Agent_City=request.POST['Agent_City']
       Agent_State=request.POST['Agent_State']
       Agent_Zip=request.POST['Agent_Zip']
       Agent_Cell_Phone=request.POST['Agent_Cell_Phone']

       print(BrokerRecordOfCompany,OpenAdvanceswihOther, Agent_First_Name,Agent_Last_Name,Agent_City,Agent_State,Agent_Home_address,Agent_Zip,Agent_Cell_Phone)
       
       ins=RemainingFormRecords(BrokerRecordOfCompany=BrokerRecordOfCompany, OpenAdvanceswihOther=OpenAdvanceswihOther)
       ins=Agent( Agent_First_Name= Agent_First_Name, 
       Agent_Last_Name= Agent_Last_Name,
       Agent_Home_address =Agent_Home_address ,
       Agent_City=Agent_City,
       Agent_State=Agent_State,
       Agent_Zip=Agent_Zip,
       Agent_Cell_Phone=Agent_Cell_Phone
       )
       ins.save()
    return render(request, 'home/SalesInfoForm.html')

def BrokerInfoForm(request):
    if request.method=="POST":
        Property_Address=request.POST.get('Property_Address')
        Property_City=request.POST.get('Property_City') 
        Property_State=request.POST.get('Property_State')
        Property_Zip=request.POST.get('Property_Zip')
        Property_Seller_Name=request.POST.get('Property_Seller_Name')
        Property_Buyer_Name =request.POST.get('Property_Buyer_Name')
        Property_Final_Price =request.POST.get('Property_Final_Price')
        Property_Closing_Date =request.POST.get('Property_Closing_Date')
        Property_Short_Sale=request.POST.get('Property_Short_Sale')

        Net_Commission=request.POST.get('Net_Commission')
        Selling_or_Listing=request.POST.get('Selling_or_Listing')
        Transaction_completein_12months=request.POST.get('Transaction_completein_12months')
        Pedning_Transaction=request.POST.get('Pedning_Transaction')
        Non_pending_Transaction=request.POST.get('Non_pending_Transaction')

        Closing_Company=request.POST.get('Closing_Company')
        Escrow=request.POST.get('Escrow')
        ClosingCompany_address=request.POST.get('ClosingCompany_address')
        ClosingCompany_city=request.POST.get('ClosingCompany_city')
        ClosingCompany_State=request.POST.get('ClosingCompany_State')
        ClosingCompany_Zip=request.POST.get('ClosingCompany_Zip')
        ClosingCompany_Cell_Phone=request.POST.get('ClosingCompany_Cell_Phone')
        ClosingCompany_Contact=request.POST.get('ClosingCompany_Contact')
        ClosingCompany_Email=request.POST.get('ClosingCompany_Email')

        
        print(Property_Address,Property_City,Property_State,Property_Zip,Property_Seller_Name,Property_Buyer_Name,Property_Final_Price,Property_Closing_Date ,Property_Short_Sale,)
        print(Net_Commission,Selling_or_Listing,Transaction_completein_12months,Pedning_Transaction,Non_pending_Transaction)
        print( Closing_Company,Escrow,ClosingCompany_address,ClosingCompany_city,ClosingCompany_State,ClosingCompany_Zip,ClosingCompany_Cell_Phone,ClosingCompany_Contact,ClosingCompany_Email)

        ins=Property(Property_Address=Property_Address,
            Property_City=Property_City,
            Property_State=Property_State,
            Property_Zip=Property_Zip,
            Property_Seller_Name=Property_Seller_Name,
            Property_Final_Price=Property_Final_Price,
            Property_Closing_Date=Property_Closing_Date,
            Property_Buyer_Name=Property_Buyer_Name
           )
        ins1=SalesInformation_AgentDetail(Net_Commission=Net_Commission,
            Selling_or_Listing=Selling_or_Listing,
            Transaction_completein_12months= Transaction_completein_12months,
            Pedning_Transaction=Pedning_Transaction,
            Non_pending_Transaction=Non_pending_Transaction)   


        ins2=ClosingCompanyDetails(Closing_Company= Closing_Company,
        Escrow=Escrow,ClosingCompany_address=ClosingCompany_address,
        ClosingCompany_city=ClosingCompany_city,
        ClosingCompany_State=ClosingCompany_State,
        ClosingCompany_Zip=ClosingCompany_Zip,
        ClosingCompany_Cell_Phone=ClosingCompany_Cell_Phone,
        ClosingCompany_Contact=ClosingCompany_Contact,
        ClosingCompany_Email=ClosingCompany_Email
        )

        ins2.save()
        ins1.save()
        ins.save()
    return render(request,'home/BrokerInfoForm.html')

def BankInformation(request):
    if request.method=="POST":
        Broker_CompanyName=request.POST['Broker_CompanyName']
        Broker_address=request.POST['Broker_address']
        Broker_City=request.POST['Broker_City']
        Broker_State=request.POST['Broker_State']
        Broker_Zip=request.POST['Broker_Zip']
        Company_Cell_Phone=request.POST['Company_Cell_Phone']
        BrokerFirst_Name=request.POST['BrokerFirst_Name']
        Broker_Last_Name=request.POST['Broker_Last_Name']
        Broker_Email=request.POST['Broker_Email']
        
        print(Broker_CompanyName,Broker_address,Broker_Zip,Company_Cell_Phone,BrokerFirst_Name,Broker_Email)

        ins=Broker(Broker_CompanyName=Broker_CompanyName,
        Broker_address=Broker_address,
        Broker_City=Broker_City,
        Broker_State=Broker_State,
        Broker_Zip=Broker_Zip,
        Company_Cell_Phone=Company_Cell_Phone,
        BrokerFirst_Name=BrokerFirst_Name,
        Broker_Last_Name=Broker_Last_Name,
        Broker_Email=Broker_Email)

        ins.save()
    return render(request, 'home/BankInfo.html')


def DocumentUpload(request):
    if request.method=="POST":
        Agent_Bank_Name=request.POST['Agent_Bank_Name']
        Agent_Statement_Address=request.POST['Agent_Statement_Address']
        Account_Holder_Name=request.POST['Account_Holder_Name']
        Agent_Account_type=request.POST['Agent_Account_type']
        Agent_Statement_City=request.POST['Agent_Statement_City']
        Agent_Statement_State=request.POST['Agent_Statement_State']
        Routing=request.POST['Routing']
        Account_number=request.POST['Account_number']
        Agent_Statement_Zip =request.POST['Agent_Statement_Zip']

        print(Agent_Bank_Name, Agent_Statement_Address, Account_Holder_Name, Agent_Account_type,Agent_Statement_City,
        Agent_Statement_State,Routing,Account_number,Agent_Statement_Zip)

        ins=AgentBankDetails(Agent_Bank_Name=Agent_Bank_Name,
        Agent_Statement_Address=Agent_Statement_Address,
        Account_Holder_Name=Account_Holder_Name,
        Agent_Account_type=Agent_Account_type,
        Agent_Statement_City=Agent_Statement_City,
        Agent_Statement_State=Agent_Statement_State,
        Routing=Routing,
        Account_number=Account_number,
        Agent_Statement_Zip=Agent_Statement_Zip)

        ins.save()
    return render(request,'home/DocumentUpload.html')

def ThankYouApplication(request):
    if request.method=="POST":
        
        return render(request, 'home/ThanksApplication.html')