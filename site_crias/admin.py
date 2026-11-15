# Painel da ONG: mostra as tabelas em /painel-crias/

from django.contrib import admin

from .models import Mensagem, Padrinho, Voluntario


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "area_interesse", "criado_em")


class PadrinhoAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "valor", "criado_em")


class MensagemAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "criado_em")


admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Padrinho, PadrinhoAdmin)
admin.site.register(Mensagem, MensagemAdmin)
