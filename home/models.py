from curses.ascii import NUL
from django.db import models
import datetime
from django import forms
from accounts.models import User
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from django.utils.timezone import now


# Create your models here.
class AmountRequest(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.EmailField(null=True)
    amount = models.CharField(max_length=5)

class Agent(models.Model):
    Agent_ID = models.AutoField(primary_key=True)
    Agent_First_Name = models.CharField(max_length=15)
    Agent_Last_Name = models.CharField(max_length=15)
    Agent_Email = models.EmailField(max_length=254)
    Agent_Cell_Phone = models.CharField(max_length=15)
    Agent_Home_address = models.CharField(max_length=50)
    Agent_City = models.CharField(max_length=15)
    Agent_State = USStateField(blank=True)
    Agent_Zip = USZipCodeField(blank=True)


class Application(models.Model):
    count = models.AutoField(primary_key=True, default=1)
    application_id = models.CharField(max_length=15)
    created_on = models.DateField(default=now)
    completed_on = models.DateField(default=now)
    
    @property
    def application_id():
        strr = "QCA"
        dt_object = str(datetime.strptime('%y/%m/%d'))
        no = str(1000 + self.count)
        return '{}{}-{}'.format(strr, dt_object, no)
    


class Property(models.Model):
    Property_Address = models.CharField(max_length=50)
    Property_City = models.CharField(max_length=15) 
    Property_State = USStateField(blank=True)
    Property_Zip = USZipCodeField(blank=True)
    Property_Seller_Name = models.CharField(max_length=15)
    Property_Buyer_Name = models.CharField(max_length=15)
    Property_Final_Price = models.IntegerField()
    Property_Closing_Date = models.DateField(default=now)
    Poperty_Short_Sale = models.CharField(max_length=15)

class AgentBankDetails(models.Model):
    Agent_ID = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Agent_Bank_Name = models.CharField(max_length=15,null=True)
    Agent_Statement_Address = models.CharField(max_length=15,null=True)
    Account_number=models.IntegerField(null=True)
    Routing=models.CharField(max_length=15,null=True)
    Account_Holder_Name=models.CharField(max_length=50,null=True)
    Agent_Account_type = models.CharField(max_length=50,null=True)
    Agent_Statement_City = models.CharField(max_length=15,null=True)
    Agent_Statement_State = USStateField(blank=True)
    Agent_Statement_Zip = USZipCodeField(blank=True)

class ContactUs(models.Model):
    Name=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    Subject=models.CharField(max_length=40)
    Message=models.TextField()

class SalesInformation_AgentDetail(models.Model):
    Net_Commission = models.IntegerField()
    Selling_or_Listing=models.CharField(max_length=15)
    Transaction_completein_12months=models.IntegerField()
    Pedning_Transaction=models.IntegerField()
    Non_pending_Transaction=models.IntegerField()

class RemainingFormRecords(models.Model):
    BrokerRecordOfCompany=models.CharField(max_length=5)
    OpenAdvanceswihOther=models.CharField( max_length=5 )


class ClosingCompanyDetails(models.Model):
    Closing_Company=models.CharField(max_length=20)
    Escrow=models.CharField(max_length=20)
    ClosingCompany_address = models.CharField(max_length=50)
    ClosingCompany_city = models.CharField(max_length=50)
    ClosingCompany_State = USStateField(blank=True)
    ClosingCompany_Zip = USZipCodeField(blank=True)
    ClosingCompany_Cell_Phone = models.CharField(max_length=15)
    ClosingCompany_Contact=models.CharField(max_length=20)
    ClosingCompany_Email = models.EmailField(max_length=254)
   
class Broker(models.Model):
    Broker_CompanyName=models.CharField(max_length=30)
    Broker_address = models.CharField(max_length=50)
    Broker_City = models.CharField(max_length=15)
    Broker_State = USStateField(blank=True)
    Broker_Zip = USZipCodeField(blank=True)
    Company_Cell_Phone = models.CharField(max_length=15)
    BrokerFirst_Name = models.CharField(max_length=15)
    Broker_Last_Name = models.CharField(max_length=15)
    Broker_Email = models.EmailField(max_length=254)

class Documents(forms.Form):
    purchase_agreement = models.FileField(upload_to='documents/')
   
   

    