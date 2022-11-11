from django.contrib import admin
from django.contrib import admin
from .models import Agent,AmountRequest,Property,AgentBankDetails,ContactUs

admin.site.register(Agent)
admin.site.register(AmountRequest)
admin.site.register(Property)
admin.site.register(AgentBankDetails)
admin.site.register(ContactUs)


