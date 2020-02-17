from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View

from administrador.models import Administrador
from organizador.forms import OrganizadorForm
from organizador.models import Organizador


class NovoOrganizador(View):
    def get(self, request):
        template_name = 'administrador/novo_organizador.html'
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
                return redirect('administrador:listar-organizadores')


class ListarOrganizador(View):
    def get(self, request):
        template_name = 'administrador/listar_organizadores.html'
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
                is_admin = True
            except:
                user = Organizador.objects.get(user=request.user)
        organizadores = Organizador.objects.filter(is_active=True)
        context = {'user': user, 'organizadores': organizadores, 'is_admin': is_admin}
        return render(request, template_name, context)


class EditarOrganizador(View):
    def get(self, request):
        template_name = 'administrador/editar_organizador.html'
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
