from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from organizador.models import Organizador
from administrador.models import Administrador
from .models import Evento, Dia, Atividade, Palestrante, Patrocinador

from .forms import EventoForm, AtividadeForm, PalestranteForm, PatrocinadorForm


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


@login_required
def dias_atividades(request, slug, dia):
    template_name = 'eventos/listagem-dias.html'
    e = Evento.objects.get(slug=slug)
    user = Organizador.objects.get(user=request.user)
    dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
    dias = Dia.objects.filter(evento=e)
    atividades = Atividade.objects.filter(dia=dia_atual)
    context = {'user': user, 'evento': e, 'dia_atual': dia_atual, 'dias': dias, 'atividades': atividades}
    return render(request, template_name, context)


class NovaAtividade(View):
    @method_decorator(login_required)
    def get(self, request, slug, dia):
        template_name = 'eventos/nova-atividade.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
        atividade_form = AtividadeForm()
        context = {'user': user, 'evento': e,
                   'dia_atual': dia_atual,
                   'atividade_form': atividade_form}
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, dia):
        template_name = 'eventos/nova-atividade.html'
        e = get_object_or_404(Evento, slug=slug)
        user = Organizador.objects.get(user=request.user)
        dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
        atividade_form = AtividadeForm(request.POST)
        if not request.POST['nome']:
            atividade_form.add_error('nome', 'Este campo é obrigatório')
        if not request.POST['horario']:
            atividade_form.add_error('horario', 'Este campo é obrigatório')
        if atividade_form.is_valid():
            a = atividade_form.save(commit=False)
            a.dia = dia_atual
            a.save()
            return redirect(to='eventos:dias-atividades', slug=e.slug, dia=dia_atual, permanent=True)
        context = {'user': user, 'evento': e,
                   'dia_atual': dia_atual,
                   'atividade_form': atividade_form}
        return render(request, template_name, context)


class EditarAtividade(View):
    @method_decorator(login_required)
    def get(self, request, slug, dia, apk):
        template_name = 'eventos/editar-atividade.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
        a = get_object_or_404(Atividade, pk=apk)
        atividade_form = AtividadeForm(instance=a)
        context = {'user': user, 'evento': e,
                   'dia_atual': dia_atual,
                   'atividade_form': atividade_form,
                   'apk': a.pk}
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, dia, apk):
        success_message = None
        template_name = 'eventos/nova-atividade.html'
        e = get_object_or_404(Evento, slug=slug)
        user = Organizador.objects.get(user=request.user)
        dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
        a = get_object_or_404(Atividade, pk=apk)
        atividade_form = AtividadeForm(request.POST, instance=a)
        if not request.POST['nome']:
            atividade_form.add_error('nome', 'Este campo é obrigatório')
        if not request.POST['horario']:
            atividade_form.add_error('horario', 'Este campo é obrigatório')
        if atividade_form.is_valid():
            a = atividade_form.save(commit=False)
            a.dia = dia_atual
            a.save()
            success_message = 'Informações salvas com sucesso!'
            context = {'user': user, 'evento': e,
                       'dia_atual': dia_atual,
                       'atividade_form': atividade_form,
                       'success_message': success_message}
            return render(request, template_name, context)
        context = {'user': user, 'evento': e,
                   'dia_atual': dia_atual,
                   'atividade_form': atividade_form}
        return render(request, template_name, context)


@login_required
def palestrantes(request, slug):
    template_name = 'eventos/listagem-palestrantes.html'
    e = Evento.objects.get(slug=slug)
    user = Organizador.objects.get(user=request.user)
    p = Palestrante.objects.filter(evento=e)
    context = {'user': user, 'evento': e, 'palestrantes': p}
    return render(request, template_name, context)


class NovoPalestrante(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        template_name = 'eventos/novo-palestrante.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        p_form = PalestranteForm()
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        template_name = 'eventos/novo-palestrante.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        p_form = PalestranteForm(request.POST, request.FILES)
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.evento = e
            p.save()
            success_message = 'Informações salvas com sucesso!'
            context = {
                'user': user, 'evento': e,
                'p_form': p_form,
                'success_message': success_message
            }
            return redirect(to='eventos:palestrantes', slug=e.slug)
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)


class EditarPalestrante(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        template_name = 'eventos/editar-palestrante.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        p = get_object_or_404(Palestrante, pk=pk)
        p_form = PalestranteForm(instance=p)
        context = {
            'user': user, 'evento': e,
            'p_form': p_form,
            'pk': pk,
            'p': p
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, pk):
        template_name = 'eventos/editar-palestrante.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        p = get_object_or_404(Palestrante, pk=pk)
        p_form = PalestranteForm(request.POST, request.FILES, instance=p)
        if p_form.is_valid():
            p.save()
            success_message = 'Informações salvas com sucesso!'
            context = {
                'user': user,
                'evento': e,
                'p_form': p_form,
                'success_message': success_message,
                'pk': pk,
                'p': p
            }
            return render(request, template_name, context, success_message)
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)


@login_required
def patrocinadores(request, slug):
    template_name = 'eventos/listagem-patrocinadores.html'
    e = Evento.objects.get(slug=slug)
    user = Organizador.objects.get(user=request.user)
    p = Patrocinador.objects.filter(evento=e)
    context = {'user': user, 'evento': e, 'patrocinadores': p}
    return render(request, template_name, context)


class EditarPatrocinador(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        template_name = 'eventos/editar-patrocinador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        p = get_object_or_404(Patrocinador, pk=pk)
        p_form = PatrocinadorForm(instance=p)
        context = {
            'user': user,
            'evento': e,
            'p_form': p_form,
            'pk': pk,
            'p': p
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, pk):
        template_name = 'eventos/editar-patrocinador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        p = get_object_or_404(Patrocinador, pk=pk)
        p_form = PatrocinadorForm(request.POST, request.FILES, instance=p)
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.evento = e
            p.save()
            success_message = 'Informações salvas com sucesso!'
            context = {
                'user': user,
                'evento': e,
                'p_form': p_form,
                'success_message': success_message,
                'pk': pk,
                'p': p
            }
            return render(request, template_name, context, success_message)
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)


class NovoPatrocinador(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        template_name = 'eventos/novo-patrocinador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        p_form = PatrocinadorForm()
        context = {
            'user': user,
            'evento': e,
            'p_form': p_form,
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        template_name = 'eventos/editar-patrocinador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        p_form = PatrocinadorForm(request.POST, request.FILES)
        if p_form.is_valid():
            p = p_form.save(commit=False)
            p.evento = e
            p.save()
            return redirect(to='eventos:patrocinadores', slug=slug)
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)
