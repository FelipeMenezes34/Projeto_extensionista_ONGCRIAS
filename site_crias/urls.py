# Endereço de cada página do site

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quem-somos/", views.sobre, name="sobre"),
    path("projetos/", views.projetos, name="projetos"),
    path("voluntario/", views.voluntario, name="voluntario"),
    path("padrinho/", views.padrinho, name="padrinho"),
    path("doacao/", views.doacao, name="doacao"),
    path("contato/", views.contato, name="contato"),
    path("privacidade/", views.privacidade, name="privacidade"),
]
