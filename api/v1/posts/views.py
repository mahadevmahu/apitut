from django.shortcuts import render
from django.http import HttpResponse
from web.models import Post
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .serializers import PostSerializer
from rest_framework import status
import datetime


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def create_post(request):
    serialzed = PostSerializer(data=request.data)
    print(request.data)

    if serialzed.is_valid():
        serialzed.save()

        response_data = {
            "StatusCode":6000,
            'data':serialzed.data
        }
        return Response(response_data,status=status.HTTP_200_OK)
    else:
        response_data = {
            "StatusCode":6001,
            'message':serialzed._errors
        }
        return Response(response_data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def edit_post(request,pk):
    serialzed = PostSerializer(data=request.data)
    print(request.data)
    instance = None

    if Post.objects.filter(id=pk).exists():
        instance = Post.objects.get(id=pk)

    if instance:
        if serialzed.is_valid():
            image = request.data.get('image')
            print(image,'Hellooooo')
            serialzed.update(instance, serialzed.data)
            instance.image = image
            instance.date_time = datetime.datetime.now()
            instance.save()

            response_data = {
                "StatusCode":6000,
                'data':serialzed.data
            }
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            response_data = {
                "StatusCode":6001,
                'message':serialzed._errors
            }
            return Response(response_data,status=status.HTTP_200_OK)
    else:
        response_data = {
            "StatusCode":6001,
            'message':'Post Not Found'
        }
        return Response(response_data,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def posts(request):
    instances = Post.objects.all()

    query = request.GET.get('q')
    if query:
        instances = instances.filter(title__icontains=query,description__icontains=query)

    serialzed = PostSerializer(instances,many=True,context={'request':request})

    response_data = {
        "StatusCode":6000,
        'data':serialzed.data
    }

    return Response(response_data,status=status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def post(request,pk):
    instance = None
    if Post.objects.filter(id=pk).exists():
        instance = Post.objects.get(id=pk)
    if instance:
        serialzed = PostSerializer(instance,context={'request':request})

        response_data = {
            "StatusCode":6000,
            'data':serialzed.data
        }
    else:
        response_data = {
            "StatusCode":6001,
            'message':'Customer not found'
        }

    return Response(response_data,status=status.HTTP_200_OK)