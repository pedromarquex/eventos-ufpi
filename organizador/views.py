from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from eventos.models import Evento
from .models import Organizador

from .forms import OrganizadorForm


@login_required
def meus_eventos(request):
    template_name = 'organizador/meus_eventos.html'
    is_admin = False
    user = Organizador.objects.get(user=request.user)

    eventos = Evento.objects.filter(organizador=user)

    if len(eventos) == 0:
        eventos = None

    context = {'user': user, 'is_admin': is_admin, 'eventos': eventos}
    return render(request, template_name, context)


class Perfil(View):
    @method_decorator(login_required)
    def get(self, request):
        is_admin = False
        user = Organizador.objects.get(user=request.user)
        template_name = 'organizador/perfil.html'
        organizador_form = OrganizadorForm(instance=user)
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'is_admin': is_admin
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        mensagem_sucesso = None
        user = Organizador.objects.get(user=request.user)
        template_name = 'organizador/perfil.html'
        organizador_form = OrganizadorForm(request.POST, instance=user)
        if organizador_form.is_valid():
            organizador_form.save()
            context = {
                'user': user,
                'organizador_form': organizador_form,
                'is_admin': False,
                'mensagem_sucesso': mensagem_sucesso
            }
            return render(request, template_name, context)
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'is_admin': False,
            'mensagem_sucesso': mensagem_sucesso
        }
        return render(request, template_name, context)


class Senha(View):
    @method_decorator(login_required)
    def get(self, request):
        is_admin = False
        user = Organizador.objects.get(user=request.user)
        senha_form = PasswordChangeForm(request.user)
        template_name = 'organizador/senha.html'
        context = {
            'user': user,
            'senha_form': senha_form,
            'is_admin': is_admin
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        is_admin = False
        user = Organizador.objects.get(user=request.user)
        template_name = 'organizador/senha.html'
        senha_form = PasswordChangeForm(request.user, request.POST)
        if senha_form.is_valid():
            u = senha_form.save()
            update_session_auth_hash(request, u)
            senha_form = PasswordChangeForm(request.user)
            context = {
                'user': user,
                'senha_form': senha_form,
                'is_admin': is_admin,
                'mensagem_sucesso': 'Senha alterada com sucesso'
            }
            return render(request, template_name, context)
        context = {
            'user': user,
            'senha_form': senha_form,
            'is_admin': is_admin,
        }
        return render(request, template_name, context)


class NovaSenha(View):
    @method_decorator(login_required)
    def get(self, request):
        org = Organizador.objects.get(user=request.user)
        if org.has_changed_password:
            return redirect('core:index')
        is_admin = False
        user = Organizador.objects.get(user=request.user)
        senha_form = SetPasswordForm(request.user)
        template_name = 'organizador/nova_senha.html'
        context = {
            'user': user,
            'is_admin': is_admin,
            'senha_form': senha_form
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        senha_form = SetPasswordForm(request.user, request.POST)
        if senha_form.is_valid():
            senha_form.save()
            org = Organizador.objects.get(user=request.user)
            org.has_changed_password = True
            org.save()
            return redirect('core:login')
        template_name = 'organizador/nova_senha.html'
        context = {
            'senha_form': senha_form
        }
        return render(request, template_name, context)
