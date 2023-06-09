from django.contrib import admin
from .models import Filme, Episodios, Usuario
from django.contrib.auth.admin import UserAdmin


# Register your models here.

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_visto',)})
)

UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodios)
admin.site.register(Usuario, UserAdmin)
