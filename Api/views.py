from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from travello.models import Destination
from Api.serializers import mySerializer


@api_view(['GET', ])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def api_destination_details(request, name):
    try:
        dests = Destination.objects.get(name=name)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = mySerializer(dests)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_destination_edit(request, name):
    try:
        dest = Destination.objects.get(name=name)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = mySerializer(dest, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'edit successful'
        return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_destination_delete(request, name):
    try:
        dest = Destination.objects.get(name=name)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = dest.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['success'] = 'delete failure'
        return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def api_destination_add(request):
    if request.method == 'POST':
        serializer = mySerializer(data=request.data)
        # print(serializer)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'add successful'
            print("itssssssssssss")
        return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_destinations_details(request):
    try:
        dests = Destination.objects.all()
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = mySerializer(dests,many=True)
        return Response(serializer.data)
