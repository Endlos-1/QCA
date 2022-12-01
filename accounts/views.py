from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, RedirectView, ListView, DetailView, UpdateView
from home.models import AmountRequest
from .models import User
from .forms import UserRegistrationForm, UserLoginForm, ProfileUpdateForm
from django.shortcuts import render,redirect

class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/Register.html'
    success_url = '/signin'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if "next" in self.request.POST:
            return self.request.POST["next"]
        else:
            return self.success_url 
    
        

    def post(self, request, *args, **kwargs):

        user_form = self.form_class(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            email = user_form.cleaned_data.get("email")
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            subject = "You Account has been Successfully created"
            message = f"Welocme to ENDLOS"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('accounts:signin')
        else:
            return render(request, 'accounts/Register.html', {'form': user_form})


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/'
    request_url = '/applynow'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
    
    def get_success_url(self):
        if "next" in self.request.POST:
            return self.request.POST["next"]
        else:
            return self.success_url 

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        

        return HttpResponseRedirect(self.get_success_url())
        # return super(Login, self).form_valid(form)
       

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/signin'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)

def QcaAdmin(request):
    return render(request, 'accounts/AdminPanel.html')
