# Cada função aqui é uma página do site.
# Nos formulários: pegamos os dados do request.POST, conferimos e salvamos no banco.

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import Mensagem, Padrinho, Voluntario


def telefone_valido(telefone):
    # o telefone precisa ter DDD + número (10 ou 11 números)
    quantidade = 0
    for letra in telefone:
        if letra.isdigit():
            quantidade = quantidade + 1
    return quantidade == 10 or quantidade == 11


def avisar_ong(assunto, texto):
    # Manda um e-mail para a ONG. Se der erro, o cadastro continua salvo no banco.
    if settings.EMAIL_HOST_PASSWORD == "":
        return
    try:
        send_mail(assunto, texto, settings.EMAIL_HOST_USER, [settings.EMAIL_DESTINO])
    except Exception as erro:
        print("Não foi possível enviar o e-mail:", erro)


# ----- Páginas que só mostram informação -----

def index(request):
    return render(request, "index.html")


def sobre(request):
    return render(request, "sobre.html")


def projetos(request):
    return render(request, "projetos.html")


def doacao(request):
    return render(request, "doacao.html")


def privacidade(request):
    return render(request, "privacidade.html")


# ----- Páginas com formulário -----

def voluntario(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()[:100]
        email = request.POST.get("email", "").strip()[:100]
        telefone = request.POST.get("telefone", "").strip()[:20]
        area = request.POST.get("area_interesse", "")
        aceitou = request.POST.get("consentimento") == "on"

        if nome != "" and "@" in email and telefone_valido(telefone) and area != "" and aceitou:
            Voluntario.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                area_interesse=area,
                consentimento=True,
            )
            avisar_ong(
                "Novo voluntário no site",
                f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nÁrea de interesse: {area}",
            )
            messages.success(request, "Cadastro realizado! Obrigado por querer fazer parte da CRIAS.")
            return redirect("voluntario")

        messages.error(request, "Confira os dados (telefone com DDD) e aceite a política de privacidade.")

    # request.POST devolve o que a pessoa digitou, para não perder se der erro
    return render(request, "voluntario.html", {"dados": request.POST})


def padrinho(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()[:100]
        email = request.POST.get("email", "").strip()[:100]
        telefone = request.POST.get("telefone", "").strip()[:20]
        aceitou = request.POST.get("consentimento") == "on"

        # o valor vem como texto, então transformamos em número
        try:
            valor = float(request.POST.get("valor", "0").replace(",", "."))
        except ValueError:
            valor = 0

        if nome != "" and "@" in email and telefone_valido(telefone) and valor >= 50 and aceitou:
            Padrinho.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                valor=valor,
                consentimento=True,
            )
            avisar_ong(
                "Novo padrinho no site",
                f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nValor mensal: R$ {valor:.2f}",
            )
            messages.success(request, "Obrigado por apadrinhar! Entraremos em contato em breve.")
            return redirect("padrinho")

        messages.error(request, "Confira os dados (valor mínimo de R$ 50,00) e aceite a política de privacidade.")

    return render(request, "padrinho.html", {"dados": request.POST})


def contato(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()[:100]
        email = request.POST.get("email", "").strip()[:100]
        texto = request.POST.get("mensagem", "").strip()[:2000]
        aceitou = request.POST.get("consentimento") == "on"

        if nome != "" and "@" in email and texto != "" and aceitou:
            Mensagem.objects.create(nome=nome, email=email, mensagem=texto, consentimento=True)
            avisar_ong(
                "Nova mensagem no site",
                f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{texto}",
            )
            messages.success(request, "Mensagem enviada! Responderemos em breve.")
            return redirect("contato")

        messages.error(request, "Preencha todos os campos e aceite a política de privacidade.")

    return render(request, "contato.html", {"dados": request.POST})
