from django.test import TestCase


class TestHomeView(TestCase):
    def test_home_view(self):
        response = self.client.get('/')
        
        self.assertTemplateUsed(response, 'home/index.html')
