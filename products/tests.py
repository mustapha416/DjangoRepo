from django.test import TestCase

from products.models import Offer


class OfferModelTest(TestCase):
    def test_offer_string_representation_uses_existing_fields(self):
        offer = Offer.objects.create(code="SAVE10", description="10% off", discount=10)

        self.assertEqual(str(offer), "SAVE10 - 10.0% off")
