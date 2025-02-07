import datetime

from django.test import TestCase, Client
from django.urls import reverse
from .models import ChuzoReview
from model_bakery import baker
import json


class ChuzosListViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('chuzos')
        # Create test reviews using model-bakery
        self.chuzos = baker.make(
            'ChuzoReview',
            _quantity=2,
            _fill_optional=True  # This fills all fields with random data
        )
    def tearDown(self):
        ChuzoReview.objects.all().delete()

    def test_view_returns_200(self):
        """Test that the view returns a successful response"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Test that the view uses the correct template"""
        response = self.client.get(self.list_url)
        self.assertTemplateUsed(response, 'chuzos/chuzos_list.html')

    def test_context_contains_chuzos(self):
        """Test that the context contains the chuzos data as JSON"""
        response = self.client.get(self.list_url)
        context_chuzos = json.loads(response.context['chuzos'])

        # Check that we have the correct number of reviews
        self.assertEqual(len(context_chuzos), 2)
        # Check that our baked objects are in the response
        db_chuzo_ids = set(ChuzoReview.objects.values_list('id', flat=True))
        response_ids = {chuzo['id'] for chuzo in context_chuzos}
        self.assertEqual(db_chuzo_ids, response_ids)

    def test_empty_database(self):
        """Test the view with no data in the database"""
        ChuzoReview.objects.all().delete()

        response = self.client.get(self.list_url)
        context_chuzos = json.loads(response.context['chuzos'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(context_chuzos), 0)

    def test_json_serialization(self):
        """Test that the JSON serialization handles dates correctly"""
        # Create a chuzo with specific date for testing
        specific_chuzo = baker.make(
            'ChuzoReview',
            created_at='2025-02-06'
        )

        response = self.client.get(self.list_url)
        context_chuzos = json.loads(response.context['chuzos'])
        # Find our specific chuzo in the response
        test_chuzo = next(c for c in context_chuzos if c['id'] == specific_chuzo.id)

        # Verify date serialization
        self.assertEqual(test_chuzo['created_at'], '2025-02-06 00:00:00+00:00')

    def test_large_dataset(self):
        """Test the view with a larger dataset"""
        # Create 50 more reviews
        baker.make('ChuzoReview', _quantity=50)

        response = self.client.get(self.list_url)
        context_chuzos = json.loads(response.context['chuzos'])

        self.assertEqual(len(context_chuzos), 52)  # 50 new + 2 from setUp
        self.assertEqual(response.status_code, 200)
