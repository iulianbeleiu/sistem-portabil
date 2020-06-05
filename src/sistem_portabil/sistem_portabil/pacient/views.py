from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Adresa, DateMedicale, Recomandari, Pacient
from sistem_portabil.fisa_medicala.models import AvertizarePacient, AdresaPacient, DateMedicalePacient, RecomandariPacient
import random
import string

@csrf_exempt
def test(request):
    return JsonResponse({})

@csrf_exempt
def fixture(request):
    [User.objects.create_user('pacient' + str(i), password='pacient', is_staff=True) for i in range(1, 20)]
    pacient = Group.objects.get(name='Pacient')
    [pacient.user_set.add(User.objects.get(username='pacient' + str(i))) for i in range(1, 20)]

    [User.objects.create_user('doctor' + str(i), password='doctor', is_staff=True) for i in range(1, 6)]
    doctor = Group.objects.get(name='Doctor')
    [doctor.user_set.add(User.objects.get(username='doctor' + str(i))) for i in range(1, 6)]

    for i in range(1, 50):
        Recomandari.objects.create(
            tip_recomandare=''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
            durata_zilnica=random.randint(1, 100),
            alte_indicatii=''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            user=User.objects.get(username='doctor' + str(random.randint(1, 4)))
        )
        DateMedicale.objects.create(
            istoric_medical=''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            alergii=''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            consultatii_cardiologice=''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            user=User.objects.get(username='doctor' + str(random.randint(1, 4)))
        )
        Adresa.objects.create(
            tara='Romania',
            judet=''.join(random.choices(string.ascii_lowercase + string.digits, k=5)),
            localitate=''.join(random.choices(string.ascii_lowercase + string.digits, k=7)),
            strada=''.join(random.choices(string.ascii_lowercase + string.digits, k=6)),
            scara=''.join(random.choices(string.ascii_lowercase + string.digits, k=1)),
            numar=random.randint(1, 100),
            apartament=random.randint(1, 100),
            user=User.objects.get(username='doctor'+str(random.randint(1, 4)))
        )

    return HttpResponse('OK')