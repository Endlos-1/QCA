from django.db import models
from accounts.models import User
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from django.utils.timezone import now


# Create your models here.
class AmountRequest(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.EmailField()
    amount = models.IntegerField()

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

class Property(models.Model):
    Property_Address = models.CharField(max_length=50)
    Property_City = models.CharField(max_length=15)
    Property_State = USStateField(blank=True)
    Property_Zip = USZipCodeField(blank=True)
    Property_Seller_Name = models.CharField(max_length=15)
    Property_Buyer_Name = models.CharField(max_length=15)
    Property_Final_Price = models.IntegerField()
    Property_Closing_Date = models.DateField(default=now)
    Poperty_Short_Sale = models.BooleanField(default=True)


class AgentBankDetails(models.Model):
    Agent_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Agent_Bank_Name = models.CharField(max_length=15)
    Agent_address = models.CharField(max_length=50)
    Agent_City = models.CharField(max_length=15)
    Agent_State = USStateField(blank=True)
    Agent_Zip = USZipCodeField(blank=True)


class ContactUs(models.Model):
    Name=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    Subject=models.CharField(max_length=40)
    Message=models.TextField()