from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from core.models import User

class UserRegisterView(View):
    template_name = 'core/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        telephone_number = request.POST.get('telephone_number')

        if not all([username, email, password, telephone_number]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            telephone_number=telephone_number
        )

        return JsonResponse({'status': 'success', 'message': 'User registered successfully'})
