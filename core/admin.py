from django.contrib import admin
admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Título HTML do Site'

from core.models import Tema
from core.models import ItemTema
from core.models import Aluguel
from core.models import Endereco
from core.models import Cliente


class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valorAluguel', 'corToalha')
    search_fields = ('nome',)

class ItemTemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

class AluguelAdmin(admin.ModelAdmin):
    list_display = ('dataFesta', 'horaInicio', 'horaTermino', 'valorCobrado')
    list_filter = ('dataFesta',)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep')
    search_fields = ('logradouro', )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    search_fields = ('nome',)
    list_filter = ('nome',)

admin.site.register(Tema, TemaAdmin)
admin.site.register(ItemTema, ItemTemaAdmin)
admin.site.register(Aluguel, AluguelAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Cliente, ClienteAdmin)
