from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from organizador.models import Organizador
from administrador.models import Administrador


def index(request):
    return redirect('eventos:index')


class Login(View):
    def get(self, request):
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
            except:
                user = Organizador.objects.get(user=request.user)
        login_form = AuthenticationForm()
        template_name = 'core/login.html'
        context = {'login_form': login_form, 'user': user}
        return render(request, template_name, context)

    def post(self, request):
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            try:
                Administrador.objects.get(user=user)
                return redirect('administrador:listar-organizadores')
            except:
                org = Organizador.objects.get(user=user)
                if not org.has_changed_password:
                    return redirect('organizador:nova-senha')
                return redirect('organizador:meus-eventos')

        else:
            template_name = 'core/login.html'
            erro_login = "Usuário ou senha inválida."
            login_form = AuthenticationForm()
            if request.user.is_anonymous:
                user = request.user
            else:
                try:
                    user = Administrador.objects.get(user=request.user)
                except:
                    user = Organizador.objects.get(user=request.user)
            context = {'user': user, 'erro_login': erro_login, 'login_form': login_form}
            return render(request, template_name, context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('eventos:index')
