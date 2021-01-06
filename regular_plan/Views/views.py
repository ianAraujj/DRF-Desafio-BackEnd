# rest_framework

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.exceptions import MethodNotAllowed

# regular_plan
from regular_plan.models import RegularPlan
from regular_plan.serializers import RegularPlanSerializer


class RegularPlanPublishListView(viewsets.ModelViewSet):

    permission_classes = [AllowAny]
    http_method_names = ['get']
    queryset = RegularPlan.objects.filter(publish=True)
    serializer_class = RegularPlanSerializer



class RegularPlanView(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put']
    queryset = RegularPlan.objects.all()
    serializer_class = RegularPlanSerializer

    def create(self, request):

        request.data['owner'] = request.user.pk
        post_data = request.data
        
        serializer = RegularPlanSerializer(data=post_data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"detail": "Regular Plan Created"}, status=status.HTTP_201_CREATED)
        else:
            errors = serializer.errors
            return Response(data={"detail": errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        queryset = RegularPlan.objects.filter(owner=request.user.pk)
        queryset_serializer = self.serializer_class(queryset, many=True)

        return Response(data={"detail": queryset_serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        
        queryset = get_object_or_404(RegularPlan, pk=pk)

        if queryset.owner == None or queryset.owner.pk != request.user.pk:
            return Response(data={"detail": "Unauthorized User"}, status=status.HTTP_401_UNAUTHORIZED)

        post_data = request.data
        serializer = RegularPlanSerializer(queryset, data=post_data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"detail": "Regular Plan Updated"}, status=status.HTTP_200_OK)
        else:
            errors = serializer.errors
            return Response(data={"detail": errors}, status=status.HTTP_400_BAD_REQUEST)