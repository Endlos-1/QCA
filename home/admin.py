from django.contrib import admin
from django.contrib import admin
from .models import Agent,AmountRequest,Property,AgentBankDetails,ContactUs,SalesInformation_AgentDetail,RemainingFormRecords,ClosingCompanyDetails,Broker

admin.site.register(Agent)
admin.site.register(AmountRequest)
admin.site.register(Property)
admin.site.register(AgentBankDetails)
admin.site.register(ContactUs)
admin.site.register(SalesInformation_AgentDetail)
admin.site.register(RemainingFormRecords)
admin.site.register(ClosingCompanyDetails)
admin.site.register(Broker)



