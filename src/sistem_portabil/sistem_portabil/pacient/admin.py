from django.contrib import admin
from .models import Pacient, DateMedicale, Recomandari, Adresa


class Adresadmin(admin.ModelAdmin):
    list_display = ('id', 'tara', 'judet', 'localitate', 'strada', 'user')
    search_fields = ('tara', 'judet', 'localitate')
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(Adresadmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Adresa, Adresadmin)


class PacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nume', 'prenume', 'user')
    list_filter = ('nume', 'prenume')
    search_fields = ('nume', 'prenume')
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PacientAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

admin.site.register(Pacient, PacientAdmin)


@admin.register(DateMedicale)
class DateMedicaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'istoric_medical', 'alergii', 'consultatii_cardiologice')
    list_filter = ('istoric_medical', 'alergii', 'consultatii_cardiologice')
    search_fields = ('istoric_medical', 'alergii', 'consultatii_cardiologice')


@admin.register(Recomandari)
class RecomandariAdmin(admin.ModelAdmin):
    list_display = ('id', 'tip_recomandare', 'durata_zilnica', 'alte_indicatii')
    list_filter = ('tip_recomandare', 'durata_zilnica', 'alte_indicatii')
    search_fields = ('tip_recomandare', 'durata_zilnica', 'alte_indicatii')
