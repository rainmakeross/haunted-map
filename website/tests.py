from django.test import TestCase
from model_mommy import mommy
# Create your tests here.

from website.models import Newsletter, HauntedLocation

class NewsletterEmailUnicode(TestCase):
    def test_unicode(self):

        newsletter = Newsletter(email='test@test.com')
        self.assertEquals(str(newsletter),'test@test.com')


