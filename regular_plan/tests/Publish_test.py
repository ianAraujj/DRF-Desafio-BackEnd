from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from regular_plan.models import RegularPlan
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
import json
from regular_plan.seeds import insertSeeds

class RegularPlanPublishTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        insertSeeds()

    
    def test_sucess_route(self):
        url = reverse('publish-true')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_sucess_regular_plan(self):

        count_regular_plan = RegularPlan.objects.filter(publish=True).count()

        url = reverse('publish-true')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(count_regular_plan, len(response.data))
