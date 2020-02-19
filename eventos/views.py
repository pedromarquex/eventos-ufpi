from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from organizador.models import Organizador
from administrador.models import Administrador
from .models import Evento

from .forms import EventoForm


class Index(View):
    def get(self, request):
        is_admin = False
        template_name = 'eventos/index.html'
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
                is_admin = True
            except:
                user = Organizador.objects.get(user=request.user)
        eventos = Evento.objects.all()
        context = {'user': user, 'is_admin': is_admin, 'eventos': eventos}
        return render(request, template_name, context)


class EditarEventoInfo(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        success_message = None
        template_name = 'eventos/editar-evento-info-contato.html'
        e = Evento.objects.get(slug=slug)
        evento_form = EventoForm(instance=e)
        user = Organizador.objects.get(user=request.user)
        context = {'evento_form': evento_form, 'user': user, 'evento': e, 'success_message': success_message}
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        template_name = 'eventos/editar-evento-info-contato.html'
        e = Evento.objects.get(slug=slug)
        evento_form = EventoForm(request.POST, request.FILES, instance=e)
        if not request.POST['onde']:
            evento_form.add_error('onde', 'Este campo é obrigatório')
        if not request.POST['quando']:
            evento_form.add_error('quando', 'Este campo é obrigatório')
        if not request.POST['sobre']:
            evento_form.add_error('sobre', 'Este campo é obrigatório')
        if not request.FILES and not e.banner:
            evento_form.add_error('banner', 'Este campo é obrigatório')
        if not request.POST['endereco']:
            evento_form.add_error('endereco', 'Este campo é obrigatório')
        if not request.POST['telefone']:
            evento_form.add_error('telefone', 'Este campo é obrigatório')
        if not request.POST['email']:
            evento_form.add_error('email', 'Este campo é obrigatório')
        if not request.POST['instagram']:
            evento_form.add_error('instagram', 'Este campo é obrigatório')
        user = Organizador.objects.get(user=request.user)
        if evento_form.is_valid():
            evento_form.save()
            success_message = "Informações alteradas com sucesso!"
            context = {'evento_form': evento_form, 'user': user, 'evento': e, 'success_message': success_message}
            return render(request, template_name, context)
        context = {'evento_form': evento_form, 'user': user, 'evento': e}
        return render(request, template_name, context)
