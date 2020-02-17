from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from eventos.models import Evento
from organizador.models import Organizador


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
