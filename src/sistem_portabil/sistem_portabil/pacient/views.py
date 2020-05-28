from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
    return JsonResponse({})