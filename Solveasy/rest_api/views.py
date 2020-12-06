from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Authority.models import problem, otherDetails
from .serializer import AvblSerializer, DetailSerializer


class FoodAvailable(APIView):
    @staticmethod
    def get(request):
        list1 = problem.objects.all()
        serializer = AvblSerializer(list1, many=True)
        return Response(serializer.data)


class FoodRequest(APIView):
    @staticmethod
    def get(request):
        list1 = FoodReq.objects.all()
        serializer = ReqSerializer(list1, many=True)
        return Response(serializer.data)


class Details(APIView):
    @staticmethod
    def get(request):
        list1 = otherDetails.objects.all()
        serializer = DetailSerializer(list1, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, "rest_api/api_home.html")

