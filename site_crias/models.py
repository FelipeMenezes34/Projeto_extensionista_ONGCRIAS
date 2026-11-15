# Cada classe aqui vira uma tabela no banco de dados

from django.db import models


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    area_interesse = models.CharField(max_length=100)
    consentimento = models.BooleanField(default=False)  # aceitou a política de privacidade
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "voluntarios"

    def __str__(self):
        return self.nome


class Padrinho(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    consentimento = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "padrinhos"

    def __str__(self):
        return self.nome


class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
    consentimento = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mensagens"

    def __str__(self):
        return self.nome
