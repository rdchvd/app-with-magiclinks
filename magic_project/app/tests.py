from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='kek@email.com')
        #u = User.objects.get(email='kek@email.com')
        #print(u)
