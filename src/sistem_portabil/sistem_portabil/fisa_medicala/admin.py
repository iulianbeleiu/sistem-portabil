from django.contrib import admin
from django.contrib.auth.models import User
from .models import RecomandariPacient, DateMedicalePacient, AvertizarePacient
from sistem_portabil.pacient.models import Pacient, Recomandari, DateMedicale


class RecomandariPacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'pacient', 'recomandari')
    exclude = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(RecomandariPacientAdmin, self).get_queryset(request)
        try:
            if not request.user.is_superuser:
                return qs.filter(pacient=Pacient.objects.get(user_pacient=request.user.id).id)
            return qs
        except:
            return qs

    def render_change_form(self, request, context, *args, **kwargs):
        # context['adminform'].form.fields['pacient'].queryset = Pacient.objects.filter(user=request.user.id)
        # context['adminform'].form.fields['recomandari'].queryset = Recomandari.objects.filter(user=request.user.id)
        return super(RecomandariPacientAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(RecomandariPacient, RecomandariPacientAdmin)


class DateMedicalePacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'pacient', 'date_medicale')
    exclude = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(DateMedicalePacientAdmin, self).get_queryset(request)
        try:
            if not request.user.is_superuser:
                return qs.filter(pacient=Pacient.objects.get(user_pacient=request.user.id).id)
            return qs
        except:
            return qs

    def render_change_form(self, request, context, *args, **kwargs):
        # context['adminform'].form.fields['pacient'].queryset = Pacient.objects.filter(user=request.user.id)
        # context['adminform'].form.fields['date_medicale'].queryset = DateMedicale.objects.filter(user=request.user.id)
        return super(DateMedicalePacientAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(DateMedicalePacient, DateMedicalePacientAdmin)


class AvertizarePacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'pacient', 'avertizare')
    exclude = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(AvertizarePacientAdmin, self).get_queryset(request)
        try:
            if not request.user.is_superuser:
                return qs.filter(pacient=Pacient.objects.get(user_pacient=request.user.id).id)
            return qs
        except:
            return qs

    def render_change_form(self, request, context, *args, **kwargs):
        # context['adminform'].form.fields['pacient'].queryset = Pacient.objects.filter(user=request.user.id)
        return super(AvertizarePacientAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(AvertizarePacient, AvertizarePacientAdmin)
