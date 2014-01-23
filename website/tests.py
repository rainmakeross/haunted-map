from django.test import TestCase
from model_mommy import mommy
# Create your tests here.

from website.models import Comment, HauntedLocation

class CommentEmailIncorrectFormat(TestCase):
    def test_unicode(self):
        haunted_location = mommy.make(HauntedLocation)
        comment = Comment(comment = '', haunted_location=haunted_location)
        self.assertEquals(str(comment),'12')


