from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from core.form import UserRegisterForm


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'core/register.html', {form : 'form'})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
        return render(request, 'core/register.html', {'form': form})
