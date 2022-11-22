from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, ),
    path('agent', views.agent_Faq, name='agent_Faq'),
    path('broker', views.broker_Faq, name='broker_Faq'),
    path('applynow', views.applynow, name='applynow'),
    path('contactus', views.contactUs, name='contactUs'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('howitworks', views.howit, name="howitworks"),
    path('whycommissionadvance', views.whyadvance, name="whyadvance"),
    path('thankyou', views.thanks, name="thanks"),
    path('salesform', views.SalesInfoForm, name="SalesInfoForm"),
    path('brokerinfo', views.BrokerInfoForm, name="BrokerInfoForm"),
    path('document', views.DocumentUpload, name='DocumentUpload'),
    path('bankinfo', views.BankInfo, name="BankInfo"),
    path('thankapp', views.ThankYouApplication, name="ThankYouApplication")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)