from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, template_name='eventos/index.html')


class Eventos(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
