from django.urls import path, include
from .import views
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("signin", views.LoginView.as_view(), name="signin"),
    path("signout", views.LogoutView.as_view(), name="signout"),
    path("qcaAdmin", views.QcaAdmin, name='qcaAdmin'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html",
         email_template_name="accounts/password_reset_email.html",
         success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html", success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path(
        'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
]
