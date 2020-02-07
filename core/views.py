from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from eventos.models import Eventos

from .models import Administrador, Organizador
from .forms import OrganizadorForm


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
        erro_login = None
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            login(request, login_form.get_user())
            return redirect('core:meus-eventos')
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


class NovoOrganizador(View):
    def get(self, request):
        template_name = 'core/novo_organizador.html'
        organizador_form = OrganizadorForm()
        user_form = UserCreationForm()
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
            except:
                user = Organizador.objects.get(user=request.user)
        context = {'user': user, 'organizador_form': organizador_form, 'user_form': user_form}
        return render(request, template_name, context)

    def post(self, request):
        organizador_form = OrganizadorForm(request.POST, request.FILES)
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if organizador_form.is_valid():
                org = organizador_form.save(commit=False)
                org.user = user
                org.save()
                return redirect('core:listar-organizadores')


class ListarOrganizador(View):
    def get(self, request):
        template_name = 'core/listar_organizadores.html'
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
            except:
                user = Organizador.objects.get(user=request.user)
        organizadores = Organizador.objects.filter(is_active=True)
        context = {'user': user, 'organizadores': organizadores}
        return render(request, template_name, context)


def meus_eventos(request):
    template_name = 'eventos/meus_eventos.html'
    is_admin = None
    if request.user.is_anonymous:
        user = request.user
    else:
        try:
            user = Administrador.objects.get(user=request.user)
        except:
            user = Organizador.objects.get(user=request.user)
    eventos =
    context = {'user': user, 'is_admin': is_admin}
    return render(request, template_name, context)
