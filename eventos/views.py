from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from organizador.models import Organizador
from administrador.models import Administrador
from .models import Evento, Dia, Atividade, Palestrante, Patrocinador, Realizador, Apoiador

from .forms import EventoForm, AtividadeForm, PalestranteForm, PatrocinadorForm, RealizadorForm, ApoiadorForm, DiaForm


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
    try:
        dia_atual = get_object_or_404(Dia, evento=e, dia=dia)
    except:
        dia_atual = Dia.objects.create(dia=1, data="01/Jan", evento=e)
    dias = Dia.objects.filter(evento=e)
    atividades = Atividade.objects.filter(dia=dia_atual)
    context = {'user': user, 'evento': e, 'dia_atual': dia_atual, 'dias': dias, 'atividades': atividades}
    return render(request, template_name, context)


class NovoDia(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        template_name = 'eventos/novo-dia.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        dia_form = DiaForm()
        context = {'user': user, 'evento': e,
                   'dia_form': dia_form}
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        dia_existe = None
        template_name = 'eventos/novo-dia.html'
        e = get_object_or_404(Evento, slug=slug)
        user = Organizador.objects.get(user=request.user)

        # verificando se o dia de evento já está ocupado
        dia = int(request.POST['dia'])
        try:
            dia_existe = Dia.objects.get(dia=dia, evento=e)
        except:
            pass

        dia_form = DiaForm(request.POST)
        if dia_existe:
            dia_form.add_error('dia', 'Este dia de evento já está cadastrado')
        if not request.POST['dia']:
            dia_form.add_error('dia', 'Este campo é obrigatório')
        if not request.POST['data']:
            dia_form.add_error('data', 'Este campo é obrigatório')
        if dia_form.is_valid():
            d = dia_form.save(commit=False)
            d.evento = e
            d.save()
            return redirect(to='eventos:dias-atividades', slug=e.slug, dia=1, permanent=True)
        context = {'user': user, 'evento': e,
                   'dia_form': dia_form}
        return render(request, template_name, context)


class EditarDia(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        template_name = 'eventos/editar-dia.html'
        e = Evento.objects.get(slug=slug)
        dia = Dia.objects.get(pk=pk)
        user = Organizador.objects.get(user=request.user)
        dia_form = DiaForm(instance=dia)
        context = {
            'user': user,
            'evento': e,
            'dia_form': dia_form,
            'dia': dia
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, pk):
        dia_existe = None
        mensagem_sucesso = None
        template_name = 'eventos/editar-dia.html'
        e = get_object_or_404(Evento, slug=slug)
        user = Organizador.objects.get(user=request.user)

        # verificando se o dia de evento já está ocupado
        dia = int(request.POST['dia'])
        try:
            dia_existe = Dia.objects.get(dia=dia, evento=e)
        except:
            pass

        d = Dia.objects.get(pk=pk)
        dia_form = DiaForm(request.POST, instance=d)
        if dia_existe and dia != d.dia:
            dia_form.add_error('dia', 'Este dia de evento já está cadastrado')
        if not request.POST['dia']:
            dia_form.add_error('dia', 'Este campo é obrigatório')
        if not request.POST['data']:
            dia_form.add_error('data', 'Este campo é obrigatório')
        if dia_form.is_valid():
            d = dia_form.save(commit=False)
            d.evento = e
            d.save()
            mensagem_sucesso = 'Informações alteradas com sucesso!'
            context = {
                'user': user,
                'evento': e,
                'dia_form': dia_form,
                'dia': d,
                'mensagem_sucesso': mensagem_sucesso
            }
            return render(request, template_name, context)
        context = {
            'user': user,
            'evento': e,
            'dia_form': dia_form,
            'dia': d
        }
        return render(request, template_name, context)


@login_required
def exclui_dia(request, slug, pk):
    try:
        d = Dia.objects.get(pk=pk)
        d.delete()
        return redirect(to='eventos:dias-atividades', slug=slug, dia=1)
    except:
        return redirect(to='eventos:dias-atividades', slug=slug, dia=1)


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
def exclui_atividade(request, slug, pk, dia):
    try:
        a = Atividade.objects.get(pk=pk)
        a.delete()
        return redirect(to='eventos:dias-atividades', slug=slug, dia=dia)
    except Exception:
        return redirect(to='eventos:dias-atividades', slug=slug, dia=dia)


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
            return redirect(to='eventos:palestrantes', slug=e.slug)
        context = {'user': user, 'evento': e,
                   'p_form': p_form}
        return render(request, template_name, context)


class EditarPalestrante(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        atividades = []
        template_name = 'eventos/editar-palestrante.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        p = get_object_or_404(Palestrante, pk=pk)
        for dia in e.dia_set.filter():
            for a in Atividade.objects.filter(dia=dia):
                atividades.append(a)
        p_form = PalestranteForm(instance=p)
        context = {
            'atividades': atividades,
            'user': user,
            'evento': e,
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
            return render(request, template_name, context)
        context = {
            'user': user,
            'evento': e,
            'p_form': p_form
        }
        return render(request, template_name, context)


@login_required
def exclui_palestrante(request, slug, pk):
    try:
        p = Palestrante.objects.get(pk=pk)
        p.delete()
        return redirect(to='eventos:palestrantes', slug=slug)
    except Exception:
        return redirect(to='eventos:palestrantes', slug=slug)


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
            return render(request, template_name, context)
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


@login_required
def exclui_patrocinador(request, slug, pk):
    try:
        p = Patrocinador.objects.get(pk=pk)
        p.delete()
        return redirect(to='eventos:patrocinadores', slug=slug)
    except Exception:
        return redirect(to='eventos:patrocinadores', slug=slug)


@login_required
def realizadores(request, slug):
    template_name = 'eventos/listagem-realizadores.html'
    e = Evento.objects.get(slug=slug)
    user = Organizador.objects.get(user=request.user)
    r = Realizador.objects.filter(evento=e)
    context = {'user': user, 'evento': e, 'realizadores': r}
    return render(request, template_name, context)


class EditarRealizador(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        template_name = 'eventos/editar-realizador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        r = get_object_or_404(Realizador, pk=pk)
        r_form = RealizadorForm(instance=r)
        context = {
            'user': user,
            'evento': e,
            'r_form': r_form,
            'pk': pk,
            'r': r
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, pk):
        template_name = 'eventos/editar-realizador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        r = get_object_or_404(Realizador, pk=pk)
        r_form = RealizadorForm(request.POST, request.FILES, instance=r)
        if r_form.is_valid():
            r.save()
            success_message = 'Informações salvas com sucesso!'
            context = {
                'user': user,
                'evento': e,
                'r_form': r_form,
                'success_message': success_message,
                'pk': pk,
                'r': r
            }
            return render(request, template_name, context)
        context = {'user': user, 'evento': e,
                   'p_form': r_form}
        return render(request, template_name, context)


class NovoRealizador(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        template_name = 'eventos/novo-realizador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        r_form = RealizadorForm()
        context = {
            'user': user,
            'evento': e,
            'r_form': r_form,
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        template_name = 'eventos/novo-realizador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        r_form = RealizadorForm(request.POST, request.FILES)
        if r_form.is_valid():
            r = r_form.save(commit=False)
            r.evento = e
            r.save()
            return redirect(to='eventos:realizadores', slug=slug)
        context = {'user': user, 'evento': e,
                   'r_form': r_form}
        return render(request, template_name, context)


@login_required
def exclui_realizador(request, slug, pk):
    try:
        r = Realizador.objects.get(pk=pk)
        r.delete()
        return redirect(to='eventos:realizadores', slug=slug)
    except Exception:
        return redirect(to='eventos:realizadores', slug=slug)


@login_required
def apoiadores(request, slug):
    template_name = 'eventos/listagem-apoiadores.html'
    e = Evento.objects.get(slug=slug)
    user = Organizador.objects.get(user=request.user)
    a = Apoiador.objects.filter(evento=e)
    context = {'user': user, 'evento': e, 'apoiadores': a}
    return render(request, template_name, context)


class EditarApoiador(View):
    @method_decorator(login_required)
    def get(self, request, slug, pk):
        template_name = 'eventos/editar-apoiador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        a = get_object_or_404(Apoiador, pk=pk)
        a_form = RealizadorForm(instance=a)
        context = {
            'user': user,
            'evento': e,
            'a_form': a_form,
            'pk': pk,
            'a': a
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug, pk):
        template_name = 'eventos/editar-apoiador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        a = get_object_or_404(Apoiador, pk=pk)
        a_form = ApoiadorForm(request.POST, request.FILES, instance=a)
        if a_form.is_valid():
            a.save()
            success_message = 'Informações salvas com sucesso!'
            context = {
                'user': user,
                'evento': e,
                'a_form': a_form,
                'success_message': success_message,
                'pk': pk,
                'a': a
            }
            return render(request, template_name, context)
        context = {'user': user, 'evento': e,
                   'p_form': a_form}
        return render(request, template_name, context)


class NovoApoiador(View):
    @method_decorator(login_required)
    def get(self, request, slug):
        template_name = 'eventos/novo-apoiador.html'
        user = Organizador.objects.get(user=request.user)
        e = Evento.objects.get(slug=slug)
        a_form = ApoiadorForm()
        context = {
            'user': user,
            'evento': e,
            'a_form': a_form,
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request, slug):
        template_name = 'eventos/novo-apoiador.html'
        e = Evento.objects.get(slug=slug)
        user = Organizador.objects.get(user=request.user)
        a_form = ApoiadorForm(request.POST, request.FILES)
        if a_form.is_valid():
            a = a_form.save(commit=False)
            a.evento = e
            a.save()
            return redirect(to='eventos:apoiadores', slug=slug)
        context = {'user': user, 'evento': e,
                   'r_form': a_form}
        return render(request, template_name, context)


@login_required
def exclui_apoiador(request, slug, pk):
    try:
        a = Apoiador.objects.get(pk=pk)
        a.delete()
        return redirect(to='eventos:apoiadores', slug=slug)
    except Apoiador.DoesNotExist:
        return redirect(to='eventos:apoiadores', slug=slug)


def evento(request, slug):
    a = []
    e = get_object_or_404(Evento, slug=slug)
    template_name = 'eventos/evento.html'
    p = e.palestrante_set.all()
    pa = e.patrocinador_set.all()
    r = e.realizador_set.all()
    ap = e.apoiador_set.all()
    d = e.dia_set.all().order_by('dia')

    for dia in d:
        a.append([at for at in Atividade.objects.filter(dia=dia)])

    context = {
        'evento': e,
        'palestrantes': p,
        'dias': d,
        'atividades': a,
        'patrocinadores': pa,
        'realizadores': r,
        'apoiadores': ap,
    }
    return render(request, template_name, context)


def palestrante_detalhe(request, slug, pk):
    p = get_object_or_404(Palestrante, pk=pk)
    template_name = 'eventos/palestrante-detalhe.html'
    context = {'palestrante': p, 'slug': slug}
    return render(request, template_name, context)
