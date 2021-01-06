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

class RegularPlanListUserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        insertSeeds()

    
    def test_list_regular_plan_sucess(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        url = reverse('regular-plan')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)

    def test_list_regular_plan_count(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        url = reverse('regular-plan')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['detail']), 2)

    def test_list_regular_plan_verify(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        url = reverse('regular-plan')

        response = self.client.get(url, format='json')

        for plan in response.data['detail']:
            self.assertEqual(plan['owner'], user.pk)
