# Site da ONG CRIAS

Site institucional feito com Python, Django, MySQL e Bootstrap 5.

## Como o projeto está organizado
```
manage.py          comando principal do Django
config/            configurações (settings.py) e endereço do painel (urls.py)
site_crias/        o site em si
    models.py      as tabelas do banco (voluntarios, padrinhos, mensagens)
    views.py       o que cada página faz
    urls.py        o endereço de cada página
    admin.py       o que aparece no painel da ONG
templates/         as páginas em HTML
static/            css, js e imagens
```

## Onde mudar cada coisa
| Quero mudar                              | Arquivo                                        |
|------------------------------------------|------------------------------------------------|
| Telefone, e-mail, Instagram              | `templates/base.html` (rodapé), `contato.html`, `index.html` |
| Chave PIX, bancos e QR Code              | `templates/doacao.html` e `static/img/qrcode-pix.png` |
| Textos das páginas                       | `templates/*.html`                             |
| Cores e visual                           | `static/css/style.css`                         |
| Logo, mascote e fotos                    | `static/img/`                                  |

Dica: no VS Code, use Ctrl+Shift+F para procurar o telefone antigo em todos os arquivos.

## Rodar no computador
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py makemigrations site_crias
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Site: http://127.0.0.1:8000  |  Painel: http://127.0.0.1:8000/painel-crias/

Para usar MySQL: rode o `database.sql` no Workbench, coloque `DB_ENGINE=mysql` no `.env` e a senha em `DB_PASSWORD`.

## Publicar (ongcrias.org.br)
No `.env` do servidor: `DEBUG=False`, uma `SECRET_KEY` nova e grande, `ALLOWED_HOSTS` e
`CSRF_TRUSTED_ORIGINS` com o domínio (modelo no `.env.example`), e os dados do MySQL.
Depois: `python manage.py collectstatic`, `python manage.py migrate` e `python manage.py createsuperuser`.
O site precisa estar em HTTPS. Nunca envie o `.env` para o GitHub.

## Segurança
- Senhas fora do código (arquivo `.env`).
- Formulários com proteção CSRF e gravação pelo Django (evita SQL Injection).
- Painel com login e senha; HTTPS e cookies protegidos quando `DEBUG=False`.
- LGPD: caixa de consentimento nos formulários e página de política de privacidade.
