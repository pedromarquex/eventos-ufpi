from django.contrib import admin
from .models import Dia
from .models import Atividade
from .models import Evento
from .models import Patrocinador
from .models import Realizador
from .models import Apoiador
from .models import Palestrante

admin.site.register(Dia)
admin.site.register(Atividade)
admin.site.register(Evento)
admin.site.register(Patrocinador)
admin.site.register(Realizador)
admin.site.register(Apoiador)
admin.site.register(Palestrante)
