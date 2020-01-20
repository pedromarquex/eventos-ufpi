from django.shortcuts import render
from django.views import View
from core.models import Organizador, Administrador


class Index(View):
    def get(self, request):
        template_name = 'eventos/index.html'
        if request.user.is_anonymous:
            user = request.user
        else:
            try:
                user = Administrador.objects.get(user=request.user)
            except:
                user = Organizador.objects.get(user=request.user)
        context = {'user': user}
        return render(request, template_name, context)


class Eventos(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
