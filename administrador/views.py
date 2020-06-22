from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import UserCreationForm

from administrador.models import Administrador
from organizador.forms import OrganizadorForm
from organizador.models import Organizador

from .forms import CustomUsernameForm


class NovoOrganizador(View):
    @method_decorator(login_required)
    def get(self, request):
        template_name = 'administrador/novo_organizador.html'
        is_admin = None
        organizador_form = OrganizadorForm()
        user_form = UserCreationForm()
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
                is_admin = True
            except:
                return redirect(to='core:sistema')
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'user_form': user_form,
            'is_admin': is_admin
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        organizador_form = OrganizadorForm(request.POST)
        user_form = UserCreationForm(request.POST)
        if organizador_form.is_valid() and user_form.is_valid():
            u = user_form.save()
            org = organizador_form.save(commit=False)
            org.user = u
            org.save()
            return redirect('administrador:listar-organizadores')
        user = Administrador.objects.get(user=request.user)
        template_name = 'administrador/novo_organizador.html'
        is_admin = True
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'user_form': user_form,
            'is_admin': is_admin
        }
        return render(request, template_name, context)


class ListarOrganizador(View):
    @method_decorator(login_required)
    def get(self, request):
        is_admin = None
        template_name = 'administrador/listar_organizadores.html'

        organizadores = None

        full_name = ''
        username = ''

        try:
            full_name = request.GET['nome']
        except:
            pass

        try:
            username = request.GET['usuario']
        except:
            pass

        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
                is_admin = True
            except:
                user = Organizador.objects.get(user=request.user)

        if len(full_name) > 0 and len(username) > 0:
            organizadores = Organizador.objects.filter(full_name__icontains=full_name, user__username__iexact=username)
        elif len(full_name) > 0:
            organizadores = Organizador.objects.filter(full_name__icontains=full_name)
        elif len(username) > 0:
            organizadores = Organizador.objects.filter(user__username__icontains=username)
        else:
            organizadores = Organizador.objects.all()
        context = {'user': user, 'organizadores': organizadores, 'is_admin': is_admin}
        return render(request, template_name, context)


@login_required
def excluir_organizador(request, pk):
    get_object_or_404(Administrador, user=request.user)
    organizador = Organizador.objects.get(pk=pk)
    organizador.user.delete()
    organizador.delete()
    return redirect('administrador:listar-organizadores')


class EditarOrganizador(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        template_name = 'administrador/editar_organizador.html'
        user = get_object_or_404(Administrador, user=request.user)
        is_admin = True
        org = get_object_or_404(Organizador, pk=pk)
        organizador_form = OrganizadorForm(instance=org)
        username_form = CustomUsernameForm(instance=org.user)
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'username_form': username_form,
            'is_admin': is_admin
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, pk):
        template_name = 'administrador/editar_organizador.html'
        user = get_object_or_404(Administrador, user=request.user)
        is_admin = True
        org = get_object_or_404(Organizador, pk=pk)
        organizador_form = OrganizadorForm(request.POST, instance=org)
        username_form = CustomUsernameForm(request.POST, instance=org.user)
        if organizador_form.is_valid() and username_form.is_valid():
            organizador_form.save()
            username_form.save()
            success_message = 'Alterações salvas com sucesso!'
            context = {
                'user': user,
                'organizador_form': organizador_form,
                'username_form': username_form,
                'is_admin': is_admin,
                'success_message': success_message
            }
            return render(request, template_name, context)
        context = {
            'user': user,
            'organizador_form': organizador_form,
            'username_form': username_form,
            'is_admin': is_admin,
        }
        return render(request, template_name, context)
