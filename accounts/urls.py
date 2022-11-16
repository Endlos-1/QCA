from django.urls import path, include
from .import views

app_name = 'accounts'

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("signin", views.LoginView.as_view(), name="signin"),
    path("signout", views.LogoutView.as_view(), name="signout"),
    path("qcaAdmin", views.QcaAdmin,name='qcaAdmin')
]