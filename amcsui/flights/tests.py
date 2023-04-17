from django.test import TestCase

from .models import Airport, Flight
# Create your tests here.
class FLightTestCase(TestCase):
    def setUp(self):
        
        a = Airport.objects.create(code="AAA", city="A")
        b = Airport.objects.create(code="BBB", city="B")

        
        Flight.objects.create(origin=a, destination=a, duration=100)
        Flight.objects.create(origin=a, destination=b, duration=-100)
        Flight.objects.create(origin=a, destination=b, duration=100)

        #TODO add some users

    def test_departure_count(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.departure.count(),3)
        

    def test_arrival_count(self):
            a = Airport.objects.get(code="AAA")
            self.assertEqual(a.arrival.count(),1)

    def test_validation(self):
            a = Airport.objects.get(code="AAA")
            b = Airport.objects.get(code="BBB")

            a_a_100  = Flight.objects.get(origin=a, destination=a, duration=100)
            a_b_n100 = Flight.objects.get(origin=a, destination=b, duration=-100)
            a_b_100  = Flight.objects.get(origin=a, destination=b, duration=100)

            self.assertTrue(a_b_100.is_valid_flight(), "a to b with duration=100")
            self.assertFalse(a_a_100.is_valid_flight(), "a to a with duration=100")
            self.assertFalse(a_b_n100.is_valid_flight(),"a to b with duration=-100")

