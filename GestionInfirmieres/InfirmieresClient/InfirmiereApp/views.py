from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.http import HttpResponse

from InfirmiereApp.models import Infirmieres, Soins, Rapport, Prescription, \
    Passages, Tournees, NumeroTournee, Mutuelles, Medecin, Kine, Fiche, Patient, Equipe, Anamnese, Adresse
from InfirmiereApp.serializers import InfirmieresSerializer, SoinsSerializer, \
    RapportSerializer, PrescriptionSerializer, PassagesSerializer, TourneesSerializer, NumeroTourneeSerializer, \
    MedecinSerializer, MutuellesSerializer, KineSerializer, FicheSerializer, PatientSerializer, EquipeSerializer, \
    AnamneseSerializer, AdresseSerializer


# Create your views here.

@csrf_exempt
def infirmiereApi(request, id=0):
    if request.method == 'GET':
        infirmieres = Infirmieres.objects.all()
        infirmieres_serializer = InfirmieresSerializer(infirmieres, many=True)
        return JsonResponse(infirmieres_serializer.data, safe=False)
    elif request.method == 'POST':
        infirmiere_data = JSONParser().parse(request)
        infirmieres_serializer = InfirmieresSerializer(data=infirmiere_data)
        if infirmieres_serializer.is_valid():
            infirmieres_serializer.save()
            return JsonResponse("Create Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        infirmiere_data = JSONParser().parse(request)
        infirmiere = Infirmieres.objects.get(numero_inami=infirmiere_data['numero_inami'])
        infirmieres_serializer = InfirmieresSerializer(infirmiere, data=infirmiere_data)
        if infirmieres_serializer.is_valid():
            infirmieres_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        infirmiere = Infirmieres.objects.get(numero_inami=id)
        infirmiere.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@api_view(['GET'])
def ShowAll(request):
    soins = Soins.objects.all()
    serializer = SoinsSerializer(soins, many=True)
    return Response(serializer.data)



# Api soins

@api_view(['GET'])
def ShowAll(request):
    soins = Soins.objects.all()
    serializer = SoinsSerializer(soins, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewSoin(request, pk):
    soin = Soins.objects.get(id_soins=pk)
    serializer = SoinsSerializer(soin, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateSoin(request):
    serializer = SoinsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateSoin(request, pk):
    soin = Soins.objects.get(id_soins=pk)
    serializer = SoinsSerializer(instance=soin, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteSoin(request, pk):
    soin = Soins.objects.get(id_soins=pk)
    soin.delete()

    return Response('Items delete successfully!')


# Calendar
def home(request):
    return HttpResponse('home')



"""
@csrf_exempt
def soinsApi(request, id=0):
    if request.method == 'GET':
        soins = Soins.objects.all()
        soins_serializer = SoinsSerializer(soins, many=True)
        return JsonResponse(soins_serializer.data, safe=False)
    elif request.method == 'POST':
        soin_data = JSONParser().parse(request)
        soins_serializer = SoinsSerializer(data=soin_data)
        if soins_serializer.is_valid():
            soins_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        soin_data = JSONParser().parse(request)
        soin = Soins.objects.get(id_soins=soin_data['id_soins'])
        soins_serializer = SoinsSerializer(soin, data=soin_data)
        if soins_serializer.is_valid():
            soins_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        soin = Soins.objects.get(id_soins=id)
        soin.delete()
        return JsonResponse("Deleted Successfully", safe=False)
"""

