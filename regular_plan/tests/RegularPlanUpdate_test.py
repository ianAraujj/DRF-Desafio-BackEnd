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

class RegularPlanUpdate(TestCase):

    def setUp(self):
        self.client = APIClient()
        insertSeeds()

    def test_update_unauthorized(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        other_user = User.objects.all()[1]
        regular_plan = RegularPlan.objects.filter(owner=other_user)

        data = {
            "name": "New Name for My Regular Plan",
            "tar_included": regular_plan[0].tar_included,
            "subscription": regular_plan[0].subscription,
            "cycle": regular_plan[0].cycle,
            "type": regular_plan[0].type,
            "offer_iva": regular_plan[0].offer_iva,
            "off_peak_price": regular_plan[0].off_peak_price,
            "peak_price": regular_plan[0].peak_price,
            "unit": regular_plan[0].unit,
            "valid": regular_plan[0].valid,
            "publish": regular_plan[0].publish,
            "vat": regular_plan[0].vat
        }


        url = reverse('update-regular-plan', kwargs={'pk': regular_plan[0].pk})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    
    def test_update_sucess(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        regular_plan = RegularPlan.objects.filter(owner=user)

        data = {
            "name": "New Name for My Regular Plan",
            "tar_included": regular_plan[0].tar_included,
            "subscription": regular_plan[0].subscription,
            "cycle": regular_plan[0].cycle,
            "type": regular_plan[0].type,
            "offer_iva": regular_plan[0].offer_iva,
            "off_peak_price": regular_plan[0].off_peak_price,
            "peak_price": regular_plan[0].peak_price,
            "unit": regular_plan[0].unit,
            "valid": regular_plan[0].valid,
            "publish": regular_plan[0].publish,
            "vat": regular_plan[0].vat
        }

        url = reverse('update-regular-plan', kwargs={'pk': regular_plan[0].pk})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_name_verify(self):

        user = User.objects.all()[0]

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(token))

        regular_plan = RegularPlan.objects.filter(owner=user)

        data = {
            "name": "New Name for My Regular Plan",
            "tar_included": regular_plan[0].tar_included,
            "subscription": regular_plan[0].subscription,
            "cycle": regular_plan[0].cycle,
            "type": regular_plan[0].type,
            "offer_iva": regular_plan[0].offer_iva,
            "off_peak_price": regular_plan[0].off_peak_price,
            "peak_price": regular_plan[0].peak_price,
            "unit": regular_plan[0].unit,
            "valid": regular_plan[0].valid,
            "publish": regular_plan[0].publish,
            "vat": regular_plan[0].vat
        }

        url = reverse('update-regular-plan', kwargs={'pk': regular_plan[0].pk})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        
        regular_plan_updated = RegularPlan.objects.get(pk=regular_plan[0].pk)
        self.assertEqual(
            regular_plan_updated.name,
            "New Name for My Regular Plan"
        )