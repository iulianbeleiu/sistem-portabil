from django.contrib import admin
from django.contrib.auth.models import User
from .models import Pacient, DateMedicale, Recomandari, Adresa
from sistem_portabil.fisa_medicala.models import RecomandariPacient, DateMedicalePacient, AvertizarePacient, AdresaPacient

admin.site.site_header = "Administrare Pacienti"

class ReocomandariInline(admin.TabularInline):
    model = RecomandariPacient
    max_num = 4

class DateMedicaleInline(admin.TabularInline):
    model = DateMedicalePacient
    max_num = 1

class AvertizarePacientInline(admin.TabularInline):
    model = AvertizarePacient
    max_num = 3

class Adresadmin(admin.ModelAdmin):
    list_display = ('id', 'tara', 'judet', 'localitate', 'strada', 'user')
    search_fields = ('tara', 'judet', 'localitate')
    exclude = ['user',]
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(Adresadmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Adresa, Adresadmin)

class AdresaPacientInline(admin.TabularInline):
    model = AdresaPacient
    max_num = 1


class PacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nume', 'prenume', 'user', 'user_pacient')
    list_display_links = ('id', 'nume', 'prenume')
    search_fields = ('nume', 'prenume')
    exclude = ['user', 'date_medicale', 'recomandari', 'adresa']
    inlines = [AdresaPacientInline]
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PacientAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['user_pacient'].queryset = User.objects.filter(groups__name='Pacient')
        # context['adminform'].form.fields['adresa'].queryset = Adresa.objects.filter(user=request.user.id)
        return super(PacientAdmin, self).render_change_form(request, context, *args, **kwargs)

admin.site.register(Pacient, PacientAdmin)


class DateMedicaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'istoric_medical', 'alergii', 'consultatii_cardiologice', 'user')
    search_fields = ('istoric_medical', 'alergii', 'consultatii_cardiologice')
    exclude = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(DateMedicaleAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs


admin.site.register(DateMedicale, DateMedicaleAdmin)


class RecomandariAdmin(admin.ModelAdmin):
    list_display = ('id', 'tip_recomandare', 'durata_zilnica', 'alte_indicatii', 'user')
    search_fields = ('tip_recomandare', 'durata_zilnica', 'alte_indicatii')
    exclude = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(RecomandariAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs


admin.site.register(Recomandari, RecomandariAdmin)
