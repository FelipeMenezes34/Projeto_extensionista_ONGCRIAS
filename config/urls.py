from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("painel-crias/", admin.site.urls),  # painel da ONG (precisa de login)
    path("", include("site_crias.urls")),    # páginas do site
]
