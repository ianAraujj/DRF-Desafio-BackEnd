# rest_framework

from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.exceptions import MethodNotAllowed

# regular_plan
from regular_plan.models import RegularPlan
from regular_plan.serializers import RegularPlanSerializer


class RegularPlanPublishListView(generics.ListAPIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = RegularPlanSerializer
    permission_classes = [AllowAny]
    #pagination_class = 

    def get_queryset(self):

        queryset = RegularPlan.objects.filter(publish=True)
        return queryset