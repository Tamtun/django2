from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import RegistrationForm, EmailLoginForm
from django.contrib.auth.views import LoginView
from django.conf import settings

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            # Отправка письма
            send_mail(
                subject='Добро пожаловать!',
                message='Спасибо за регистрацию в нашем сервисе.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('home')
        return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = EmailLoginForm
    template_name = 'users/login.html'