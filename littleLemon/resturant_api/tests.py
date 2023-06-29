from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Booking
from .serializers import BookingSerializer

client = APIClient()

class BookingViewTestCase(APITestCase):
    def setUp(self):
        self.booking_data = {'first_name': 'John', 'last_name': 'Doe', 'comment': 'Test', 'guest_number': 2}
        self.response = client.post(reverse('booking-list'), self.booking_data, format='json')

    def test_create_booking(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_booking(self):
        booking = Booking.objects.get(id=1)
        serializer = BookingSerializer(booking)
        response = client.get(reverse('booking-list'))
        self.assertEqual(response.data[0], serializer.data)

class RegistrationViewTestCase(APITestCase):
    def setUp(self):
        self.registration_data = {'username': 'testuser', 'password': 'testpass'}
        self.response = client.post(reverse('registration'), self.registration_data, format='json')

    def test_create_registration(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_registration(self):
        response = client.get(reverse('registration'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)