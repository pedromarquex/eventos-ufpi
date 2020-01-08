from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):
        return render(request, template_name='core/login.html')

    def post(self, request):
        login = request.POST['login']
        password = request.POST['password']

        user = authenticate(request, username=login, password=password)

        if user is not None:
            pass
        return render(request, template_name='core/login.html')
