from django.contrib import admin
from gestao_contratos.core.models import Athlete, Address

admin.AdminSite.site_header = 'Gestão de Contratos Atletas'
admin.AdminSite.site_title = 'Administração da Gestão de contratos'
admin.AdminSite.index_title = 'Administrativo'


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


@admin.register(Athlete)
class AthleteModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'cpf', 'rg']
    inlines = [AddressInline, ]
