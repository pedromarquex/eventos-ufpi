from django.shortcuts import render
from django.views import View
from core.models import Organizador, Administrador


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
        context = {'user': user, 'is_admin': is_admin}
        return render(request, template_name, context)


class Eventos(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class EditarEvento(View):
    def get(self, request):
        template_name = 'eventos/editar_evento.html'
        return render(request, template_name)
