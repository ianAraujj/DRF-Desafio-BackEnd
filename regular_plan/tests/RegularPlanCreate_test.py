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

class RegularPlanCreateTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        insertSeeds()

    
    def test_create_success(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        data = {
            "name": "Name Test",
            "tar_included": False,
            "subscription": 89.9,
            "cycle": "Weekly",
            "type": "Simple",
            "offer_iva": True,
            "off_peak_price": 7,
            "peak_price": 3.5,
            "unit": "min",
            "valid": True,
            "publish": True,
            "vat": 90
        }

        url = reverse('regular-plan')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_create_success_publish_true(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        data = {
            "name": "Name Test",
            "tar_included": False,
            "subscription": 89.9,
            "cycle": "Weekly",
            "type": "Simple",
            "offer_iva": True,
            "off_peak_price": 7,
            "peak_price": 3.5,
            "unit": "min",
            "valid": True,
            "publish": True,
            "vat": 90
        }

        url = reverse('regular-plan')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)

        regular_plan = RegularPlan.objects.get(
            name="Name Test", 
            tar_included=False,
            subscription=89.9,
            publish=True,
            peak_price=3.5,
            vat=90
        )

        self.assertEqual(regular_plan.owner, None)

    def test_create_success_publish_false(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        data = {
            "name": "Name Test",
            "tar_included": False,
            "subscription": 89.9,
            "cycle": "Weekly",
            "type": "Simple",
            "offer_iva": True,
            "off_peak_price": 7,
            "peak_price": 3.5,
            "unit": "min",
            "valid": True,
            "publish": False,
            "vat": 90
        }

        url = reverse('regular-plan')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201) 

        regular_plan = RegularPlan.objects.get(
            name="Name Test", 
            tar_included=False,
            subscription=89.9,
            publish=False,
            peak_price=3.5,
            vat=90
        )

        self.assertEqual(regular_plan.owner.pk, user.pk)