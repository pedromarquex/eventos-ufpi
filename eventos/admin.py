from django.contrib import admin
from .models import Dia
from .models import MicroEvento
from .models import Evento
from .models import Patrocinador
from .models import Realizador
from .models import Apoiador

admin.site.register(Dia)
admin.site.register(MicroEvento)
admin.site.register(Evento)
admin.site.register(Patrocinador)
admin.site.register(Realizador)
admin.site.register(Apoiador)
